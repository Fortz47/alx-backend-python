#!/usr/bin/env python3
"""coroutine called async_generator that takes no arguments"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """coroutine called async_generator that takes no arguments"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
