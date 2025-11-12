
# Data folder contract
- raw/: immutable source files (Olist, SECOM, external). Never edit by hand.
- external/: third-party or reference data (e.g., holidays/FX tables).
- interim/: temporary, stepwise outputs during cleaning/feature steps.
- processed/: analysis-ready tables for notebooks/dashboards.
Conventions:
- CSVs: UTF-8, headers, lower_snake_case columns.
- Dates: ISO 8601 (YYYY-MM-DD), timestamps in UTC.
- IDs: stable primary keys, never reused; no leading zeros stripped.
