#!/usr/bin/env python3
"""Annotation of callable function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multplies value by multiplier"""
    def mult(x: float) -> float:
        """ returns a float value multiplied by multiplier"""
        return multiplier * x

    return mult
