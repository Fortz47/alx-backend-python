#!/usr/bin/env python3
"""Annotating a functions parameter values"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotating a functions parameter values"""
    return [(i, len(i)) for i in lst]
