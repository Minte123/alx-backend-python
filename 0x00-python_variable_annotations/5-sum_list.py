#!/usr/bin/env python3
"""Annotation of list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a float list and returns the sum as float"""
    sum: float = 0
    for val in input_list:
        sum += val
    return sum
