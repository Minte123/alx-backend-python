#!/usr/bin/env python3
""" Async Comprehensions """

from typing import List
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Collect 10 random numbers using list comprehnsion
    Returns
    -------
    list
        list of 10 random numbers from async_generator()
    """
    return [i async for i in async_generator()]
