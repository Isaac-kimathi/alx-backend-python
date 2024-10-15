#!/usr/bin/env python3
""""module for measure_runtime coroutine
execute async_comprehension four times in parallel using asyncio.gather"""

import asyncio
import time
from importlib import import_module as usage

async_comprehension = usage('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """measure the total runtime and return it"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
