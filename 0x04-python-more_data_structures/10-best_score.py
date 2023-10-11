#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        if len(list(a_dictionary.keys())) == 0:
            return (None)
        vs = list(a_dictionary.values())
        ks = list(a_dictionary.keys())
        max_s = vs[0]
        k_max = ""
        for i in range(0, len(vs)):
            if vs[i] > max_s:
                max_s = vs[i]
                k_max = ks[i]
        return (k_max)
