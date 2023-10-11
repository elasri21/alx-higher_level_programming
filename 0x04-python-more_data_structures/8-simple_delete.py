#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if len(a_dictionary) > 0:
        for k in a_dictionary.keys():
            if k == key:
                del a_dictionary[k]
                break
            else:
                continue
        return (a_dictionary)
