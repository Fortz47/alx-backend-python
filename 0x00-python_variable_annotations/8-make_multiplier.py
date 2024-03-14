#!/usr/bin/python3
"""type-annotated function make_multiplier that takes a
float multiplier as argument and returns a function that
multiplies a float by multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function make_multiplier that takes a float multiplier as
    argument and returns a function that multiplies a float by multiplier
    """
    def func(x: float) -> float:
        """returns x * A_multiplier"""
        return x * multiplier
    return func
