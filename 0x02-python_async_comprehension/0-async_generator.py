#!/usr/bin/env python3
'''
this function is a couritne that takes no arguments.
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    The coroutine will loop 10times each time async wait 1sec
    then yeild a random number between 0 - 10.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
