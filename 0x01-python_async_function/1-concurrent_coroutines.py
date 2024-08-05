#!/usr/bin/env python3
""" Multiple coroutines """
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """ Wait n """
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
