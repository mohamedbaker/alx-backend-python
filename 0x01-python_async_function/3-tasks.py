#!/usr/bin/env python3
"""
 3. Tasks : return asyncio.task with reg expression.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay, creates a task with wait_random(max_delay).
    return func
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
