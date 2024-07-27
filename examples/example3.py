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
