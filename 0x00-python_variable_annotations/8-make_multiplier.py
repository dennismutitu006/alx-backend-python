#!/usr/bin/env python3
"""Return a type annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function callable"""

    def funcMult(num: float) -> float:
        return num * multiplier
    return funcMult
