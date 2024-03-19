#!/usr/bin/env python3
"""async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. spawns wait_random n times
with the specified max_delay wait_n should return the list of
all the delays (float values). The list of the delays are in
ascending order without using sort() because of concurrency"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List
from queue import Queue


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawns wait_random n times 4 with the specified max_delay"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    result = await asyncio.gather(*tasks)
    return result
