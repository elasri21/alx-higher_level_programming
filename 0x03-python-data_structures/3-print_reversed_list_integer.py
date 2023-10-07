#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev = []
    if len(my_list) == 0:
        return
    for n in my_list:
        rev.insert(0, n)
    for i in rev:
        print("{:d}".format(i))
