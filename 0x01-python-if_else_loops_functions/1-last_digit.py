#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
mod = n if not n else n - 10 if number < 0 else n
if mod > 5:
    print(f"Last digit of {number:d} is {mod:d} and is greater than 5")
elif mod < 6 and mod != 0:
    print(f"Last digit of {number:d} is {mod:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {mod:d} and is 0")
