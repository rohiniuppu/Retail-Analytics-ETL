from __future__ import annotations

from pathlib import Path
from typing import Optional

import pandas as pd


def load_and_transform(input_path: str | Path, output_path: str | Path) -> pd.DataFrame:
    """Load raw sales CSV data, clean it, and write a transformed file."""
    input_path = Path(input_path)
    output_path = Path(output_path)

    df = pd.read_csv(input_path)

    required_columns = {"store_id", "transaction_date", "product_id", "quantity", "unit_price"}
    missing = required_columns.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    df = df.copy()
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce").astype("datetime64[ns]")
    df = df.dropna(subset=["transaction_date", "store_id", "product_id", "quantity", "unit_price"])
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    df["discount"] = pd.to_numeric(df.get("discount", 0), errors="coerce")
    df["discount"] = df["discount"].fillna(0)
    df = df[(df["quantity"] > 0) & (df["unit_price"] > 0)]
    df["discount"] = df["discount"].clip(lower=0, upper=0.99)
    df["revenue"] = (df["quantity"] * df["unit_price"]) * (1 - df["discount"])
    df = df.sort_values(["transaction_date", "store_id", "product_id"]).reset_index(drop=True)
    df.to_csv(output_path, index=False)
    return df
