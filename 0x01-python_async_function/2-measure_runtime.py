#!/usr/bin/env python3
"""Measure the runtime"""


import asyncio
import time
from typing import List
from concurrent.futures import ProcessPoolExecutor


wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


async def wait_n_async(n: int, max_delay: int = 10) -> List[float]:
    return await wait_n(n, max_delay)


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Parameters:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average execution time per iteration.
    """
    start_time = time.time()

    asyncio.run(wait_n_async(n, max_delay))

    total_time = time.time() - start_time

    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    average_time = measure_time(n, max_delay)
    print(average_time)
