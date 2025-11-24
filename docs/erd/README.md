# ForgeFlow Data Schema

The data warehouse for this project follows a **Star Schema** architecture, optimized for analytical queries.

### Schema Diagram

```mermaid
erDiagram
    FACT_PRODUCTION ||--o{ FACT_SENSORS : "has telemetry"
    FACT_PRODUCTION ||--|| DIM_ITEMS : "maps to"
    DIM_ITEMS ||--|| DIM_REVIEWS : "has feedback"
    DIM_ITEMS ||--|| DIM_ORDERS : "belongs to"

    FACT_PRODUCTION {
        string batch_id PK "Unique Batch Identifier"
        string plant "Manufacturing Facility"
        string product "Product Type"
        float defect_rate "Calculated Defect %"
        string olist_product_id FK "Link to Real World"
    }

    FACT_SENSORS {
        string batch_id FK "Link to Production"
        float sensor_pressure "PSI Reading"
        float sensor_temp "Temperature (C)"
        float sensor_vibration "Vibration (Hz)"
    }

    DIM_ITEMS {
        string product_id PK "Olist Product ID"
        string order_id FK "Link to Order"
    }

    DIM_REVIEWS {
        string review_id PK
        string order_id FK
        int review_score "1-5 Stars"
    }