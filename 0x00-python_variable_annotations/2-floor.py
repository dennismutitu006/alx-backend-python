#!/usr/bin/env python3
"""
This function is a type annotated func that takes a float
and returns an int which is floor of n
"""

import math


def floor(n: float) -> int:
    """
    This function will return the floor value.

    args:
        n(float): this is the argument to be evaluated.

    Returns:
        int: The floor value of n.
    """

    return math.floor(n)
