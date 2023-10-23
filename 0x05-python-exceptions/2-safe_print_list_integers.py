#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(0, x):
        try:
            if type(my_list[i]) == int:
                print(int(my_list[i]), end="")
                i += 1
                n += 1
            else:
                i += 1
        except:
            return
    print("")
    return (n)

