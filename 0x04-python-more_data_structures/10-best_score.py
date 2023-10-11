#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        vs = []
        ks = []
        for k, v in a_dictionary.items():
            vs.append(v)
            ks.append(k)
        max_s = vs[0]
        k_max = ""
        for i in range(0, len(vs)):
            if vs[i] > max_s:
                max_s = vs[i]
                k_max = ks[i]
        return (k_max)
    return (None)
