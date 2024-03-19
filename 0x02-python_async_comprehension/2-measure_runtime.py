#!/usr/bin/env python3
"""coroutine that will execute async_comprehension
four times in parallel using asyncio.gather"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather"""
    tasks = [asyncio.create_task(async_comprehension()) for i in range(4)]
    start = time.perf_counter()
    await asyncio.gather(*tasks)
    time_elapsed = time.perf_counter() - start
    return time_elapsed
