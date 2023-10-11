#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        new_dic = dict()
        for k, v in a_dictionary.items():
            new_dic[k] = 2 * v
        return (new_dic)
    else:
        return ({})
