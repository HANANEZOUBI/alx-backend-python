#!/usr/bin/env python3

"""
Asynchronours Caroutine
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """To wait for a random delay between 1 and 10"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
