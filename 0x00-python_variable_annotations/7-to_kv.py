#!/usr/bin/env python3
"""
a type-annotated function that takes a string k and an int or
float v as args and returns a tuple.
First element of the tuple is a str second a float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[float, int]:
    """The func will return a str and the square of v"""
    return (k, float(v ** 2))
