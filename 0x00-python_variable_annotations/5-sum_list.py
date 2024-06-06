#!/usr/bin/env python3
"""
this is a type annotated func that takes a list of floats
as args and returns their sum.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """This function will take a list of floats and sum it"""
    return sum(input_list)
