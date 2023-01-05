#!/usr/bin/env python3
"""
    Duck-typed annotation of Typevar
"""
from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """
        returns the value specified by key in dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
