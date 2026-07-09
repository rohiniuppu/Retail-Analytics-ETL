from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from retail_pipeline.etl import load_and_transform


def main() -> None:
    raw_dir = ROOT / "data" / "raw"
    warehouse_dir = ROOT / "data" / "warehouse"
    warehouse_dir.mkdir(parents=True, exist_ok=True)

    raw_files = sorted(raw_dir.glob("*.csv"))
    if not raw_files:
        print("No raw CSV files found in data/raw")
        return

    for raw_file in raw_files:
        output_file = warehouse_dir / f"{raw_file.stem}_clean.csv"
        df = load_and_transform(raw_file, output_file)
        print(f"Processed {raw_file.name} -> {output_file.name} ({len(df)} rows)")


if __name__ == "__main__":
    main()
