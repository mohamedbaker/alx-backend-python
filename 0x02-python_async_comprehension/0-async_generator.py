#!usr/bin/env python3

'''
Write a coroutine called async_generator that takes no arguments.
will loop 10 times, each time asynchronously wait 1 second
yield a random number between 0 and 10
'''
import random
import asyncio


async def async_generator():
    '''
    yield a random number between 0 and 10
    '''
    for i in range(10):
        yield random.uniform(0, 10)
    await asyncio.sleep(1)
