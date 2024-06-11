#!/usr/bin/env python3
'''
This function will import from the prev task
then write a coroutine func that takes no args.
'''

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''The coroutine will collect 10 random numbers using an async comprehen
    sing over async_generator.
    '''
    return [number async for number in async_generator()]
