```markdown
# Model Card: ForgeFlow Predictive Engine (v1)

### 📊 Model Summary
* **Architecture:** Gradient Boosting Classifier (sklearn)
* **Purpose:** Predict probability of manufacturing batch failure based on sensor telemetry.
* **Input Features:** Sensor Pressure, Temperature, Vibration, Plant Location, Product Type.
* **Target:** Binary Classification (Defect Rate > 2.5%).

### 🚀 Performance Metrics
* **F1 Score:** 0.70 (Outperformed Random Forest baseline)
* **ROC-AUC:** 0.76
* **Key Driver:** `product_type` (Microwaves are inherently high-risk).

### 💡 Strategic Simulations
The model was used to simulate two strategic interventions:
1.  **Cooling Upgrade:** Reducing sensor temp by 10% yields an **8.2% reduction** in defects.
2.  **Relocation Strategy:** Shifting production from Recife to Campinas yields **<1% improvement**, indicating the issue is Process-based, not Location-based.