# Data Area Contracts

- **raw/**: Original sources (Olist, SECOM). No edits. Include source link + checksum if possible.
- **external/**: Third-party or reference data (e.g., product catalog codes).
- **interim/**: Staged outputs from cleaning/joins; reproducible from code.
- **processed/**: Final, analysis-ready tables that dashboards/models consume.

Conventions:
- CSVs UTF-8, comma-delimited, headers present.
- Dates ISO-8601; times in UTC unless stated.
- One table = one file unless partitioned by date.
