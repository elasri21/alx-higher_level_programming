#!/usr/bin/python3
def magic_calculation(a, b):
    magic_res = 0
    for j in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            magic_res += a ** b/i
        except Exception:
            magic_res = b + a
            break
    return (magic_res)
