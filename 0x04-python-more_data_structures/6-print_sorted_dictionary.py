#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ks = []
    for k in a_dictionary.keys():
        ks.append(k)
    ks.sort()
    for i in ks:
        print("{}: {}".format(i, a_dictionary[i]))
