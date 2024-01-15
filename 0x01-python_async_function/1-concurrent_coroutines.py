#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""


import asyncio
from typing import List


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
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
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

if __name__ == "__main__":
    asyncio.run(wait_n(5, 5))
    asyncio.run(wait_n(10, 7))
    asyncio.run(wait_n(10, 0))
