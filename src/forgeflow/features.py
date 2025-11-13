import pandas as pd


def add_time_features(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """
    Add time-based features from a datetime-like column:
    - day of week
    - ISO week number
    - month
    """
    out = df.copy()
    dt = pd.to_datetime(out[date_col], utc=True, errors="coerce")
    out["dow"] = dt.dt.dayofweek
    out["week"] = dt.dt.isocalendar().week.astype(int)
    out["month"] = dt.dt.month
    return out