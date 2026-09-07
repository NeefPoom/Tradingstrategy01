"""Phase H1 — freeze baseline verification.

Stores model file hashes, feature columns, config snapshot, and package
versions at the first Phase H run. Every subsequent run verifies the frozen
model files have not changed. A hash mismatch prints a PHASE H MODEL FREEZE
VIOLATION warning.
"""
from pathlib import Path
import hashlib
import json
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

MODELS_DIR = ROOT / "models"
BASELINE_PATH = ROOT / "reports" / "phase_h_baseline.json"
REGISTRY_PATH = ROOT / "models" / "registry.json"

FROZEN_MODELS = [
    "mr_win_classifier", "mr_return_regressor", "mr_fail_classifier",
    "runner_win_classifier", "runner_return_regressor",
]

MODEL_VERSION = "H1.0"


def file_sha256(path: Path) -> str:
    """SHA-256 hex digest of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _pkg_versions() -> dict:
    from importlib.metadata import version
    out = {}
    for pkg in ["pandas", "numpy", "scikit-learn", "yfinance", "joblib", "pyarrow"]:
        try:
            out[pkg] = version(pkg)
        except Exception:
            out[pkg] = "unknown"
    return out


def build_baseline(cfg: dict) -> dict:
    """Create the frozen baseline snapshot (first Phase H run only)."""
    models = {}
    for name in FROZEN_MODELS:
        p = MODELS_DIR / f"{name}.joblib"
        if p.exists():
            models[name] = {
                "sha256": file_sha256(p),
                "modified": datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc).isoformat(),
            }
    feat_path = MODELS_DIR / "feature_columns.json"
    feat_list = json.loads(feat_path.read_text(encoding="utf-8")) if feat_path.exists() else []
    return {
        "phase_h_start": datetime.now(timezone.utc).isoformat(),
        "models": models,
        "mr_fail_threshold": 0.45,
        "tf_enabled": False,
        "data_source": "yahoo",
        "automatic_retraining": False,
        "feature_columns": feat_list,
        "config_snapshot": {"decision": cfg.get("decision", {}),
                            "phase_h": cfg.get("phase_h", {})},
        "package_versions": _pkg_versions(),
        "model_version": MODEL_VERSION,
    }


def ensure_baseline(cfg) -> dict:
    """Load existing baseline or create it on first Phase H run."""
    if BASELINE_PATH.exists():
        return json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    baseline = build_baseline(cfg)
    BASELINE_PATH.parent.mkdir(parents=True, exist_ok=True)
    BASELINE_PATH.write_text(json.dumps(baseline, indent=2), encoding="utf-8")
    if not REGISTRY_PATH.exists():
        REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
        registry = {"phase_h_baseline": {
            "version": MODEL_VERSION,
            "trained_before": datetime.now(timezone.utc).date().isoformat(),
            "mr_fail_threshold": 0.45,
            "active": True}}
        REGISTRY_PATH.write_text(json.dumps(registry, indent=2), encoding="utf-8")
    print(f"Phase H baseline created ({MODEL_VERSION}); "
          f"{len(baseline['models'])} models frozen.")
    return baseline


def verify_freeze(baseline: dict) -> dict:
    """Verify frozen model files unchanged.

    Returns {"status": "PASS"|"VIOLATION", "models": {...}} and prints
    the freeze-violation warning when a hash differs.
    """
    results = {}
    for name in FROZEN_MODELS:
        if name not in baseline.get("models", {}):
            continue
        p = MODELS_DIR / f"{name}.joblib"
        if not p.exists():
            results[name] = {"status": "MISSING"}
            print(f"WARNING: frozen model missing: {name}")
            continue
        current = file_sha256(p)
        frozen = baseline["models"][name]["sha256"]
        if current != frozen:
            print("WARNING: PHASE H MODEL FREEZE VIOLATION")
            print(f"  model file changed: {name}")
            results[name] = {"status": "CHANGED", "sha256": current}
        else:
            results[name] = {"status": "OK", "sha256": current}
    status = "PASS" if all(r["status"] == "OK" for r in results.values()) else "VIOLATION"
    return {"status": status, "models": results}


def get_model_version() -> str:
    """Active model version from registry (default H1.0)."""
    if REGISTRY_PATH.exists():
        reg = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        for k, v in reg.items():
            if v.get("active"):
                return v.get("version", MODEL_VERSION)
    return MODEL_VERSION
