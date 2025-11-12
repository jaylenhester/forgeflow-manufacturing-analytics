"""
Synthetic data generation for household appliances:
- products: microwaves, vacuums, coffee makers
- 3 plants (BR): Campinas, Manaus, Recife (example)
Outputs:
- production table
- qc_signals (SECOM-like)
- sales/shipments (Olist-like)
"""
from dataclasses import dataclass
from typing import List
import numpy as np
import pandas as pd

PRODUCTS = ["microwave", "vacuum", "coffee_maker"]
PLANTS = ["campinas", "manaus", "recife"]

@dataclass
class SynthConfig:
    n_days: int = 365
    seed: int = 42

def make_production(cfg: SynthConfig) -> pd.DataFrame:
    rng = np.random.default_rng(cfg.seed)
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=cfg.n_days, freq="D")
    rows = []
    for d in dates:
        for plant in PLANTS:
            for p in PRODUCTS:
                volume = rng.poisson(lam={"microwave":200,"vacuum":150,"coffee_maker":180}[p])
                defect_rate = rng.normal(loc={"microwave":0.03,"vacuum":0.02,"coffee_maker":0.025}[p], scale=0.005)
                rows.append((d.date(), plant, p, max(volume,0), float(max(defect_rate, 0.001))))
    return pd.DataFrame(rows, columns=["date","plant","product","units","defect_rate"])
