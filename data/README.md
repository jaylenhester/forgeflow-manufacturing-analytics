# data/

This directory stores all datasets used in the ForgeFlow project.

- `raw/`  
  Original source files exactly as downloaded (Olist, SECOM, and any other inputs).  
  **Read-only**: never modify these in-place. All cleaning happens downstream.

- `interim/`  
  Intermediate artifacts created during cleaning/transformations  
  (e.g., partially cleaned Olist orders, joined tables before final feature engineering).

- `processed/`  
  Fully cleaned, model-ready datasets.  
  These are the main inputs for modeling notebooks and dashboards.

- `external/`  
  Any third-party or auxiliary data that isn’t directly from Olist/SECOM  
  (e.g., macro indicators, currency rates, external benchmarks).


Conventions:
- CSVs UTF-8, comma-delimited, headers present.
- Dates ISO-8601; times in UTC unless stated.
- One table = one file unless partitioned by date.
