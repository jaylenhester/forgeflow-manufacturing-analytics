from pathlib import Path

# Project root = repo root (assumes this file is in src/forgeflow/)
ROOT = Path(__file__).resolve().parents[2]

DATA      = ROOT / "data"
RAW       = DATA / "raw"
EXTERNAL  = DATA / "external"
INTERIM   = DATA / "interim"
PROCESSED = DATA / "processed"

DOCS      = ROOT / "docs"
NOTEBOOKS = ROOT / "notebooks"
SQL       = ROOT / "src" / "sql"
