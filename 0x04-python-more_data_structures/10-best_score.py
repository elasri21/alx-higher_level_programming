#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        vs = list(a_dictionary.values())
        ks = list(a_dictionary.keys())
        if len(ks) == 0:
            return (None)
        max_s = a_dictionary[ks[0]]
        mx = ks[0]
        for k in ks:
            if a_dictionary[k] > max_s:
                max_s = a_dictionary[k]
                mx = k
        return (mx)
