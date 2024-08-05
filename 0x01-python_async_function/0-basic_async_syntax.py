#!/usr/bin/env python3
""" Basic async """
import asyncio
from random import uniform as ran


async def wait_random(max_delay: int = 10) -> float:
    """ Wait random """
    wait_time: float = ran(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
