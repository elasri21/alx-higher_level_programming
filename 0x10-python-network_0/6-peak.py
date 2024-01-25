#!/usr/bin/python3
"""Contains a function that returns a peak from an unsorted list"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers
    Args:
        list_of_integers: the list to get its peak"""
    if len(list_of_integers) == 0 or list_of_integers is None:
        return None
    length = len(list_of_integers)
    begain, end = 0, length - 1
    new_l = list_of_integers
    while begain < end:
        midle = begain + (end - begain) // 2
        if new_l[midle] > new_l[midle - 1] and new_l[midle] > new_l[midle + 1]:
            return new_l[midle]
        if new_l[midle - 1] > new_l[midle + 1]:
            end = midle
        else:
            begain = midle + 1
    return new_l[begain]
