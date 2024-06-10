#!/usr/bin/env python3
'''
asynchronous func wait_n that calls wait_random multiple times concurrently
and returns the sorted list of delays.
'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.

    Args:
        n: Number of times to call wait_random.
        max_delay: The maximum delay for wait_random.

    Returns:
        A sorted list of the delays.
    '''
    #  Use asyncio.gather to run wait_random concurrently for n times
    wait_times = await asyncio.gather(
        *tuple(task_wait_random(max_delay) for _ in range(n)))
    #  Sort the list of delays
    return sorted(wait_times)
