#!/usr/bin/env python3
""" module for the function measure_runtime """
from asyncio import gather
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine called measure_runtime that executes async_comprehension
    four times in parallel using asyncio.gather.
    Measures the total runtime and returns it.
    """
    start = perf_counter()
    await gather(*(async_comprehension() for _ in range(4)))
    return perf_counter() - start
