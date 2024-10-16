#!/usr/bin/env python3
"""module measures the total execution time 
for wait_n(n, max_delay)"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """returns total execution time"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return (total_time / n)
