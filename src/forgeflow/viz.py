import pandas as pd


def kpi_summary(
    df: pd.DataFrame,
    group_cols,
    kpi_col: str,
) -> pd.DataFrame:
    """
    Aggregate a KPI by group columns.

    Returns a DataFrame with mean/median/std/count sorted by mean desc.
    """
    grouped = (
        df.groupby(group_cols)[kpi_col]
        .agg(["mean", "median", "std", "count"])
        .reset_index()
        .sort_values("mean", ascending=False)
    )
    return grouped