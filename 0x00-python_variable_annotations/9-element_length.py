#!/usr/bin/env python3
"""Annotation of function parameters"""
from typing import Iterable, Sequence, Any, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return values of lst"""
    return [(i, len(i)) for i in lst]
