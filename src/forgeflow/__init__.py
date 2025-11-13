"""
ForgeFlow manufacturing analytics package.

This package contains:
- paths: project path utilities
- io: data loading/saving helpers
- synth: synthetic data generation
- clean: cleaning & standardization
- features: feature engineering
- model: modeling and evaluation
- viz: visualization helpers
"""

from . import paths, io, synth, clean, features, model, viz  # re-export modules

__all__ = ["paths", "io", "synth", "clean", "features", "model", "viz"]

