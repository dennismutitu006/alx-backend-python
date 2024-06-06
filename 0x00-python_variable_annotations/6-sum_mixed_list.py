#!/usr/bin/env python3
"""
This is a mixed list that is eirther a float or int
it returns sum of the list which is a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This func will return a float value which is the sum"""
    return sum(mxd_lst)
