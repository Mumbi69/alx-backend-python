#!/usr/bin/env python3
""" module for the function measure_runtime """
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine called measure_runtime that executes async_comprehension
    four times in parallel using asyncio.gather.
    Measures the total runtime and returns it.
    """
    start_time = time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time()

    return end_time - start_time
