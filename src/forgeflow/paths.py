import os
from pathlib import Path

# Project root (repo root)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"
EXTERNAL_DIR = DATA_DIR / "external"

def get_project_root() -> Path:
    """Return the root directory of the repository."""
    return PROJECT_ROOT


def get_data_dir(kind: str = "raw") -> Path:
    """
    Return a data subdirectory by kind: 'raw', 'interim', 'processed', 'external'.
    """
    kind = kind.lower()
    mapping = {
        "raw": RAW_DIR,
        "interim": INTERIM_DIR,
        "processed": PROCESSED_DIR,
        "external": EXTERNAL_DIR,
    }
    if kind not in mapping:
        raise ValueError(f"Unknown data kind '{kind}'. Expected one of {list(mapping)}")
    return mapping[kind]
