import pandas as pd

def kpi_summary(df: pd.DataFrame, group_cols, kpi_col: str):
    return (df.groupby(group_cols)[kpi_col]
              .agg(["mean","median","std","count"])
              .reset_index()
              .sort_values("mean", ascending=False))
