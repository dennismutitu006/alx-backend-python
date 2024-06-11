#!/usr/bin/env python3
'''
Thi function will import from the prev file
write a cooutine func that will execute async_comprehension four times
using asyncio.gather
'''

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure_runtime should measure the total time and return it '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
