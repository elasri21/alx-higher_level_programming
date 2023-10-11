#!/usr/bin/python3
def uniq_add(my_list=[]):
    if isinstance(my_list, list):
        if len(my_list) == 0:
            return (0)
        res = 0
        set1 = set(my_list)
        for n in set1:
            res += n
        return (res)
