#!/usr/bin/env python3
"""Annotation of mixed lists"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """accepts mixed list(int, float) and return their float sum"""
    sum: float = 0
    for val in mxd_lst:
        sum += val
    return sum
