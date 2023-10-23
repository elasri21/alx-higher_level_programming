#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """print elements of a list
    Args:
        x (int): number of element to be printed
        my_list (list): the list
    Return: Number of elements that printed
    """
    l = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            l += 1
        except IndexError:
            break
    print("")
    return (l)
