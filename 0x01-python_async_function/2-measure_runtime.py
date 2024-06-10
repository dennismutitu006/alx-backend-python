#!/usr/bin/env python3
'''
a function that measures the total execution time for wait_n(n, max_delay)
and returns total_time /n.
'''

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''function defination

    Args:
        n: number of times the async func will be called.
        max_delay: maximu delay time of wait_n.

    Returns:
        The average time per call.
    '''

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
