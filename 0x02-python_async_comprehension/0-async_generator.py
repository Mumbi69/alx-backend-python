#!/usr/bin/env python3
"""Async generator module"""
import asyncio
from random import uniform
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """represents the async generator function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
