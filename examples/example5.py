from time import sleep
from faker import Faker
from colorama import Fore
from single_line import SingleLine
from mock import patch

with patch('sys.stdout.isatty', return_value=False):
    with SingleLine(exit_message='done') as line:
        for _ in range(25):
            line.write(Faker().sentence(), color={'fore': Fore.YELLOW})
            sleep(.15)
