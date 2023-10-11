#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if isinstance(my_list, list):
        if len(my_list) == 0:
            return (my_list)
        new_list = []
        for n in my_list:
            if n == search:
                new_list.append(replace)
            else:
                new_list.append(n)
        return (new_list)
