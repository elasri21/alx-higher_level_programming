#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary:
        for k in list(a_dictionary.keys()):
            if k == key:
                del a_dictionary[k]
                break
            else:
                continue
        return (a_dictionary)
