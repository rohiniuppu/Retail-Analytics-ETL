from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression


def train_simple_forecast(data_path: str | Path) -> dict:
    """Train a simple linear regression model for demo forecasting.

    This is intentionally lightweight and meant as a future extension.
    """
    df = pd.read_csv(data_path)
    if df.empty:
        return {"status": "no-data"}

    df = df.copy()
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    df = df.sort_values("transaction_date")
    df["day_index"] = range(len(df))
    X = df[["day_index"]]
    y = df["revenue"]

    model = LinearRegression()
    model.fit(X, y)
    return {"status": "trained", "coef": float(model.coef_[0]), "intercept": float(model.intercept_)}
