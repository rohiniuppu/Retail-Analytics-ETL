from pathlib import Path
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from retail_pipeline.etl import load_and_transform


def test_load_and_transform_creates_clean_sales_data(tmp_path):
    input_path = tmp_path / "sales.csv"
    input_path.write_text(
        "store_id,transaction_date,product_id,quantity,unit_price,discount\n"
        "1,2024-01-01,SKU-100,2,10.0,0.0\n"
        "1,2024-01-02,SKU-100,1,10.0,1.0\n"
        "2,2024-01-03,SKU-200,3,20.0,\n"
        "2,2024-01-04,SKU-200,4,20.0,0.5\n",
        encoding="utf-8",
    )

    output_path = tmp_path / "clean_sales.csv"
    result = load_and_transform(input_path, output_path)

    assert output_path.exists()
    assert len(result) == 4
    assert result["quantity"].dtype.kind in {"i", "f"}
    assert result["unit_price"].dtype.kind in {"i", "f"}
    assert result["discount"].fillna(0).ge(0).all()
    assert result["revenue"].gt(0).all()
    assert result["transaction_date"].dtype == "datetime64[ns]"
