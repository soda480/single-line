import sys
import asyncio
import random
from faker import Faker
from single_line import SingleLine
from contextlib import nullcontext
from types import SimpleNamespace
from colorama import Fore

async def do_some_work(worker, fake, line):
    for index in range(random.randint(10, 35)):
        await asyncio.sleep(random.choice([.5, .1, .25]))
        line.write(f'worker{worker} {fake.sentence()}', color={'fore': Fore.YELLOW})

async def run(line):
    await asyncio.gather(*(do_some_work(worker, Faker(), line) for worker in range(5)))

single_line = False

if single_line:
    cm = SingleLine(exit_message='done with asyncio')
else:
    cm = nullcontext(enter_result=type('Anonymous', (object,), {'write': lambda _, m, **k: print(m, flush=True)})())

with cm as line:
    asyncio.run(run(line))
