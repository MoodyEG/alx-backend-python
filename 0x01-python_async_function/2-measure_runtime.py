#!/usr/bin/env python3
""" Measure the runtime """
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime """
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
