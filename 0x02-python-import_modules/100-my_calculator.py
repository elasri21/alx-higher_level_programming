#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv
    argv = argv[1:]
    length = len(argv)
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[0])
    b = int(argv[2])
    if argv[1] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[1] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif argv[1] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif argv[1] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
