#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if len(a_dictionary) > 0:
        new_dic = dict()
        for k, v in a_dictionary.items():
            new_dic[k] = 2 * v
        return (new_dic)
