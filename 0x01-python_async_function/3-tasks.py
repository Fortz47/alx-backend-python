#!/usr/bin/env python3
"""takes an integer max_delay and returns a asyncio.Task"""
from typing import TypeVar
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

T = TypeVar('_asyncio.Task')


def task_wait_random(max_delay: int) -> T:
    """takes an integer max_delay and returns a asyncio.Task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
