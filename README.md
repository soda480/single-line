# single-line
[![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://pybuilder.io/)
[![complexity](https://img.shields.io/badge/complexity-A-brightgreen)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)
[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-brightgreen)](https://pypi.org/project/bandit/)
[![python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-teal)](https://www.python.org/downloads/)

A context manager to facilitate printing messages to the same line. 

## Installation
```bash
pip install single-line
```

## Usage

Using the `SingleLine` context manager all calls to its `print` method will print the message to the same line. A common use case will be to use it in conjuction with a for loop as follows.

```Python
from time import sleep
from faker import Faker
from single_line import SingleLine

with SingleLine() as line:
    for _ in range(25):
        line.print(Faker().sentence())
        sleep(.15)
```

![example1](https://raw.githubusercontent.com/soda480/single-line/main/docs/images/example1.gif)


Setting `message_when_done` parameter will print a prescribed message when the context is done. The `print` method also supports printing colored messages via the [colorama](https://pypi.org/project/colorama/) module, just pass the method an optional `color` parameter consiting of a dictionary describing the `fore`, `back` and `style` you wish to the message to be printed with.

```Python
from time import sleep
from faker import Faker
from colorama import Fore
from single_line import SingleLine

with SingleLine(message_when_done='done') as line:
    for _ in range(25):
        line.print(Faker().sentence(), color={'fore': Fore.YELLOW})
        sleep(.15)

```

![example2](https://raw.githubusercontent.com/soda480/single-line/main/docs/images/example2.gif)

By default messages will be printed out to `sys.stdout` but you can print to any object with a write(string) method. This example also shows the extent of using colors when printing messages.

```Python
import sys
import random
from time import sleep
from faker import Faker
from single_line import SingleLine
from colorama import Fore, Back, Style

def get_random_fore():
    return random.choice([Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE])

def get_random_back():
    return random.choice([Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE])

def get_random_style():
    return random.choice([Style.NORMAL, Style.DIM, Style.BRIGHT])

with SingleLine(stream=sys.stderr) as line:
    for _ in range(25):
        line.print(Faker().sentence(), color={'fore': get_random_fore(), 'back': get_random_back(), 'style': get_random_style()})
        sleep(.15)
```

![example3](https://raw.githubusercontent.com/soda480/single-line/main/docs/images/example3.gif)

You can also use the `SingleLine` context manager to display messages when executing [asyncio](https://docs.python.org/3/library/asyncio.html) methods.

```Python
import asyncio
import random
from faker import Faker
from single_line import SingleLine

async def do_some_work(worker, fake, line):
    for index in range(random.randint(10, 35)):
        await asyncio.sleep(random.choice([.5, .1, .25]))
        line.print(f'worker{worker} {fake.sentence()}')

async def run(line):
    await asyncio.gather(*(do_some_work(worker, Faker(), line) for worker in range(5)))

with SingleLine(message_when_done='done with asyncio') as line:
    asyncio.run(run(line))
```

![example4](https://raw.githubusercontent.com/soda480/single-line/main/docs/images/example4.gif)

## Development

Clone the repository and ensure the latest version of Docker is installed on your development server.

Build the Docker image:
```sh
docker image build \
-t single-line:latest .
```

Run the Docker container:
```sh
docker container run \
--rm \
-it \
-v $PWD:/code \
single-line:latest \
bash
```

Execute the build:
```sh
pyb -X
```
