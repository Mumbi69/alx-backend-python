#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""


import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times
    with the specified max_delay.

    Parameters:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds
        (default is 10).

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
