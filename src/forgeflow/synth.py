"""
Synthetic data generation for household appliances.

Products:
- microwaves
- vacuums
- coffee makers

Plants (example):
- Campinas
- Manaus
- Recife

Output: production table with units + defect_rate.
"""

from dataclasses import dataclass
from typing import Sequence

import numpy as np
import pandas as pd

PRODUCTS: Sequence[str] = ("microwave", "vacuum", "coffee_maker")
PLANTS: Sequence[str] = ("campinas", "manaus", "recife")


@dataclass
class SynthConfig:
    """Config for synthetic production data."""
    n_days: int = 365
    seed: int = 42


def make_production(cfg: SynthConfig) -> pd.DataFrame:
    """
    Generate one row per product/plant/day with units and defect_rate.
    """
    rng = np.random.default_rng(cfg.seed)

    dates = pd.date_range(
        end=pd.Timestamp.today().normalize(),
        periods=cfg.n_days,
        freq="D",
    )

    records = []
    volume_lam = {"microwave": 200, "vacuum": 150, "coffee_maker": 180}
    defect_mean = {"microwave": 0.03, "vacuum": 0.02, "coffee_maker": 0.025}

    for d in dates:
        for plant in PLANTS:
            for product in PRODUCTS:
                volume = rng.poisson(lam=volume_lam[product])
                defect_rate = rng.normal(loc=defect_mean[product], scale=0.005)

                records.append(
                    {
                        "date": d.date(),
                        "plant": plant,
                        "product": product,
                        "units": max(int(volume), 0),
                        "defect_rate": float(max(defect_rate, 0.001)),
                    }
                )

    return pd.DataFrame.from_records(records)