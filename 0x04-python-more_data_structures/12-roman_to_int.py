#!/usr/bin/python3
def fix_list(nums):
    s1 = 0
    max_n = max(nums)
    for i in nums:
        if max_n > i:
            s1 += i
    return (max_n - s1)
def roman_to_int(roman_string):
    if not roman_string:
        return (0)
    if not isinstance(roman_string, str):
        return (0)
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ks = list(romans.keys())
    n = 0
    last = 0
    list_n = [0]
    for c in roman_string:
        for k in ks:
            if k == c:
                if romans.get(c) <= last:
                    n += fix_list(list_n)
                    list_n = [romans.get(c)]
                else:
                    list_n.append(romans.get(c))
                last = romans.get(c)
    n += fix_list(list_n)
    return (n)
