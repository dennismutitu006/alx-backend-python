#!/usr/bin/env python3
"""Optional and Use a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Type annotate the return elements of a tuple"""
    return (k, v * v)
