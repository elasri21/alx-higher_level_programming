#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lt = int(str(number)[-1])
if lt > 5:
    print(f"Last digit of {number} is {lt} and is greater than 5")
elif lt == 0:
    print(f"Last digit of {number} is {lt} and is 0")
elif lt < 6 and lt != 0:
    print(f"Last digit of {number} is {lt} and is less than 6 and not 0")
