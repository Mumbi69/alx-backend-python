#!/usr/bin/env python3
""" module for the function async_comprehension """
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine called async_comprehension that takes no
    arguments.
    Collects 10 random numbers using an async comprehension
    over async_generator.

    Returns the list of 10 random numbers.
    """
    return [i async for i in async_generator()]
