#!/usr/bin/env python3
"""Annotating functions"""
from typing import Optional, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Annotating functions"""
    if lst:
        return lst[0]
    else:
        return None
