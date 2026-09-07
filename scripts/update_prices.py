"""Phase G1 — refresh 1H prices from Yahoo Finance (primary data source).

Appends new bars to existing CSVs without overwriting history.
Replaces the ad-hoc download_yfinance.py loop for daily operation.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from hybrid_ml.config import asset_items, load_config
from hybrid_ml.data.yahoo_provider import update_asset_prices


def main():
    cfg = load_config()
    out = ROOT / "data" / "prices"
    out.mkdir(parents=True, exist_ok=True)

    print("Yahoo Finance 1H price update")
    print("=" * 50)
    for asset, meta in asset_items(cfg, data_collection=True):
        ticker = meta.get("yahoo")
        if not ticker:
            print(f"{asset}: no yahoo mapping in config — skipped")
            continue
        try:
            r = update_asset_prices(asset, ticker, out)
        except Exception as e:
            print(f"{asset}\n  ERROR: {e}")
            continue
        print(f"{asset}")
        print(f"  previous rows: {r.get('previous_rows', 0):,}")
        print(f"  latest downloaded: {r.get('downloaded_rows', 0):,}")
        print(f"  new rows added: {r.get('new_rows', 0)}")
        print(f"  final rows: {r.get('final_rows', 0):,}")
        if r.get("latest_timestamp"):
            print(f"  latest timestamp: {r['latest_timestamp']}")
        if r["status"] != "OK":
            print(f"  WARNING [{r['status']}]: {r['message']}")
        print()


if __name__ == "__main__":
    main()
