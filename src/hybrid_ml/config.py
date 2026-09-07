from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[2]

def load_config(path=None):
    path = Path(path) if path else ROOT / "config.yaml"
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def asset_items(cfg, *, data_collection: bool = False, forward_research: bool = False):
    """Yield configured assets filtered by universe flags."""
    for asset, meta in (cfg.get("assets") or {}).items():
        meta = meta or {}
        if data_collection and not bool(meta.get("data_collection_enabled", True)):
            continue
        if forward_research and not bool(meta.get("forward_research_enabled", True)):
            continue
        yield asset, meta


def asset_names(cfg, *, data_collection: bool = False, forward_research: bool = False) -> list[str]:
    return [asset for asset, _ in asset_items(cfg, data_collection=data_collection, forward_research=forward_research)]
