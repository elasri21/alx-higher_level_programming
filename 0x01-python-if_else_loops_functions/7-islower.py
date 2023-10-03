#!/usr/bin/env python3
def islower(c):
    chs = ""
    for ch in range(97, 123):
        chs += chr(ch)
    if c in chs:
        return True
    else:
        return False
