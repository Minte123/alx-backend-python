#!/usr/bin/env python3
""" Run time for four parallel comprehensions """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure total runtime of async_comprehension() 4 times in parallel
    Returns
    -------
    float
        total runtime in seconds
    """
    start = time.perf_counter()
    coroutines = (async_comprehension() for i in range(4))
    await asyncio.gather(*coroutines)
    end = time.perf_counter()
    return (end - start)
