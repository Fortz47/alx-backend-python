#!/usr/bin/env python3
"""using create_task from asyncio"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawns wait_random n times with the specified max_delay"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    result = await asyncio.gather(*tasks)
    return result
