#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in list(a_dictionary.values()):
        return (a_dictionary)
    new_d = {}
    for k in list(a_dictionary.keys()):
        if a_dictionary[k] == value:
            del a_dictionary[k]
        else:
            new_d[k] = a_dictionary[k]
    return (new_d)
