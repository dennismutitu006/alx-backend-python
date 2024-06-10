#!/usr/bin/env python3
'''
this func is a regular func that will import from an async func and return
a newtask
'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''will return a new created asynchronous task'''
    return asyncio.create_task(wait_random(max_delay))
