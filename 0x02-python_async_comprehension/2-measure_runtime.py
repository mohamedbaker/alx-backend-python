#!/usr/bin/env python3

'''
Module -> measure_runtime
'''

import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    execute async_comprehension 4times parallely.
    return : total runtime.
    '''

    start = time.time()
    results = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
