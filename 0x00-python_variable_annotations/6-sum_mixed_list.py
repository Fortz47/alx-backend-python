#!/usr/bin/env python3
"""type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float
"""
from typing import List


def sum_mixed_list(mxd_list: List[int | float]) -> float:
    """type-annotated function sum_mixed_list which takes a list
    mxd_lst of integers and floats and returns their sum as a float
    """
    result = 0.0
    for v in mxd_list:
        result += v
    return float(result)
