#!/usr/bin/env python3
'''
Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    wait_random Func: genrate random float num and wait for it.
    then return the num;
    '''
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
