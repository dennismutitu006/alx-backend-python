#!/usr/bin/env python3
"""
This asynchronous coroutine function takes in an integer argument
and awaits for a random delay and returns a flaot value of the delayed seconds.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """this function will wait for some seconds before output"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
