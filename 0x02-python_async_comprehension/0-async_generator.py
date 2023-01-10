#!/usr/bin/env python3
""" Async Generator """

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """ loop 10 times, asynchronously wait for 1 second, return random number
    Returns
    ------
    random number between 1 and 10
    """
    for i in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
