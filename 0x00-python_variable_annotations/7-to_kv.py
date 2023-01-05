#!/usr/bin/env python3
"""Annotation of mixed function parameters"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """accepts mixed arguments and return the square of v and str in tuple"""
    return (k, v * v)
