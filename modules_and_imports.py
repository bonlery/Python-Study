# ============================================
# MODULES AND IMPORTS
# ============================================

print("=== 1. import ===")
import math
print("math.sqrt(16):", math.sqrt(16))
print("math.pi:", math.pi)

print("\n=== 2. from ... import ... ===")
from math import sqrt, pi
print("sqrt(25):", sqrt(25))
print("pi:", pi)

print("\n=== 3. Import aliases (as) ===")
import random as r
print("random.randint(1, 10):", r.randint(1, 10))
import math as m
print("m.floor(4.7):", m.floor(4.7))

print("\n=== 4. Built-in modules ===")
import random
print("random.choice(['a','b','c']):", random.choice(['a', 'b', 'c']))

import datetime
today = datetime.date.today()
print("today:", today)
now = datetime.datetime.now()
print("now:", now.strftime("%Y-%m-%d %H:%M:%S"))

import os
print("os.getcwd():", os.getcwd())
print("current platform:", os.name)

print("\n=== 5. dir() - list names in a module ===")
print("math has 'sqrt':", "sqrt" in dir(math))

print("\n=== 6. help() - documentation ===")
# help(math)      # opens interactive help (try it yourself)
help(math.sqrt)   # shows the docstring for math.sqrt

print("\n=== 7. __name__ ===")
print("This file's __name__:", __name__)

print("\n=== 8. if __name__ == '__main__': ===")
def main():
    print("Running main() because this file is executed directly.")

if __name__ == "__main__":
    main()
# The block above only runs when this file is the main program,
# not when it is imported by another module.
