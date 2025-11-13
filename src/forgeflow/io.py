from pathlib import Path
from typing import Union

import pandas as pd

from .paths import RAW_DIR, INTERIM_DIR, PROCESSED_DIR, EXTERNAL_DIR

PathLike = Union[str, Path]


def _ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def read_raw_csv(relative_path: PathLike, **kwargs) -> pd.DataFrame:
    """Read a CSV from data/raw."""
    path = RAW_DIR / relative_path
    return pd.read_csv(path, **kwargs)


def read_external_csv(relative_path: PathLike, **kwargs) -> pd.DataFrame:
    """Read a CSV from data/external."""
    path = EXTERNAL_DIR / relative_path
    return pd.read_csv(path, **kwargs)


def read_processed_csv(relative_path: PathLike, **kwargs) -> pd.DataFrame:
    """Read a CSV from data/processed."""
    path = PROCESSED_DIR / relative_path
    return pd.read_csv(path, **kwargs)


def write_interim_csv(df: pd.DataFrame, relative_path: PathLike, **kwargs) -> Path:
    """Write an interim CSV into data/interim."""
    path = INTERIM_DIR / relative_path
    _ensure_parent(path)
    df.to_csv(path, index=False, **kwargs)
    return path


def write_processed_csv(df: pd.DataFrame, relative_path: PathLike, **kwargs) -> Path:
    """Write a processed CSV into data/processed."""
    path = PROCESSED_DIR / relative_path
    _ensure_parent(path)
    df.to_csv(path, index=False, **kwargs)
    return path
