#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lt = int(str(number)[-1])
if number < 0:
    lt = -lt
if lt > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lt))
elif lt == 0:
    print("Last digit of {} is {} and is 0".format(number, lt))
elif lt < 6 and lt != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lt))
