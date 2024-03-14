#!/usr/bin/env python3
"""Annotation functions"""

from typing import Mapping, Any, TypeVar, Optional


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Optional[T] = None):
    """Annotation functions"""
    if key in dct:
        return dct[key]
    else:
        return default
