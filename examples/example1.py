from time import sleep
from faker import Faker
from single_line import SingleLine

with SingleLine() as line:
    for _ in range(25):
        line.write(Faker().sentence())
        sleep(.15)
