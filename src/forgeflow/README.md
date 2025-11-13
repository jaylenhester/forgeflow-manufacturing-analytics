# forgeflow package

Core Python package for the ForgeFlow Manufacturing Analytics project.

## Modules

- `paths.py`  
  Centralized paths for the repository.  
  Provides helpers like `get_project_root()` and `get_data_dir(kind)`.

- `io.py`  
  Thin wrappers around file I/O for the `data/` folders  
  (`read_raw_csv`, `read_external_csv`, `write_interim_csv`, `write_processed_csv`, etc.).

- `synth.py`  
  Synthetic data generation for the household-appliance plants  
  (microwaves, vacuums, coffee makers across Brazilian plants).

- `clean.py`  
  Generic cleaning utilities (column standardization, date coercion, etc.).

- `features.py`  
  Feature engineering utilities, including:
  - date part extraction (year, month, day, week, quarter)
  - categorical encodings (e.g., one-hot for plant/product)

- `model.py`  
  Modeling pipelines (to be implemented later):
  - quality / defect classification
  - logistics / delivery-time regression

- `viz.py`  
  Visualization/export helpers for dashboards (e.g., aggregations for Tableau).

- `utils/`  
  Small generic helpers that don’t belong anywhere else (logging, validation, etc.).
