import pandas as pd

def add_time_features(df: pd.DataFrame, date_col: str):
    df = df.copy()
    dt = pd.to_datetime(df[date_col], utc=True, errors="coerce")
    df["dow"] = dt.dt.dayofweek
    df["week"] = dt.dt.isocalendar().week.astype(int)
    df["month"] = dt.dt.month
    return df
