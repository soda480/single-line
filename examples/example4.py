import asyncio
import random
from faker import Faker
from single_line import SingleLine

async def do_some_work(worker, fake, line):
    for index in range(random.randint(10, 35)):
        await asyncio.sleep(random.choice([.5, .1, .25]))
        line.write(f'worker{worker} {fake.sentence()}')

async def run(line):
    await asyncio.gather(*(do_some_work(worker, Faker(), line) for worker in range(5)))

with SingleLine(message_when_done='done with asyncio') as line:
    asyncio.run(run(line))
