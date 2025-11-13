from typing import Iterable

import pandas as pd


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Lowercase, strip, and replace spaces with underscores in column names.
    """
    out = df.copy()
    out.columns = [c.strip().lower().replace(" ", "_") for c in out.columns]
    return out


def coerce_dates(df: pd.DataFrame, cols: Iterable[str]) -> pd.DataFrame:
    """
    Convert given columns to datetime (UTC), coercing errors to NaT.
    """
    out = df.copy()
    for col in cols:
        out[col] = pd.to_datetime(out[col], errors="coerce", utc=True)
    return out