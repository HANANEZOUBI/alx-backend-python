from typing import Callable
"""
Module for 8-make_multiplier.py
"""

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
