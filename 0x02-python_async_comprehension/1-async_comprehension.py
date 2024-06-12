#!/usr/bin/env python3

'''
Import async_generator
write a coroutine called async_comprehension that takes no arguments.
collect 10 rand numbers using an async comprehensing over async_generator,
then return the 10 random numbers
'''

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    '''
    collect 10 random numbers using an async comprehensing.
    '''
    result = []
    async for i in async_generator():
        result.append(i)
    return result
