import pandas as pd

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df

def coerce_dates(df: pd.DataFrame, cols):
    df = df.copy()
    for c in cols:
        df[c] = pd.to_datetime(df[c], errors="coerce", utc=True)
    return df
