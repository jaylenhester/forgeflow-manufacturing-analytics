from __future__ import annotations

from typing import Iterable, Union, Sequence

import pandas as pd


def add_date_parts(
    df: pd.DataFrame,
    date_col: str,
    prefix: str | None = None,
    drop: bool = False,
) -> pd.DataFrame:
    """
    Add useful date-derived columns from a datetime column.

    Example outputs (if date_col='date' and prefix is None):
        - date_year
        - date_month
        - date_day
        - date_dayofweek
        - date_weekofyear
        - date_quarter
    """
    out = df.copy()

    if prefix is None:
        prefix = date_col

    # Ensure datetime
    if not pd.api.types.is_datetime64_any_dtype(out[date_col]):
        out[date_col] = pd.to_datetime(out[date_col], errors="coerce")

    dt = out[date_col].dt

    out[f"{prefix}_year"] = dt.year
    out[f"{prefix}_month"] = dt.month
    out[f"{prefix}_day"] = dt.day
    out[f"{prefix}_dayofweek"] = dt.dayofweek
    out[f"{prefix}_weekofyear"] = dt.isocalendar().week.astype("Int64")
    out[f"{prefix}_quarter"] = dt.quarter

    if drop:
        out = out.drop(columns=[date_col])

    return out


def one_hot_encode(
    df: pd.DataFrame,
    cols: Union[Sequence[str], Iterable[str]],
    drop_first: bool = False,
    dtype: type = int,
) -> pd.DataFrame:
    """
    One-hot encode the given categorical columns.

    - cols: list/iterable of column names to encode
    - drop_first: whether to drop the first level (to avoid dummy trap)
    - dtype: type of the dummy columns (int by default)
    """
    out = df.copy()
    cols = list(cols)

    dummies = pd.get_dummies(
        out[cols],
        columns=cols,
        prefix=cols,
        drop_first=drop_first,
        dtype=dtype,
    )

    # Drop original categorical columns and join encoded ones
    out = out.drop(columns=cols)
    out = pd.concat([out, dummies], axis=1)

    return out
