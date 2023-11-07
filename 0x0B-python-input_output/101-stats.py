#!/usr/bin/python3
"""contains a  script that reads stdin line by line and computes metrics"""


from sys import stdin
size = 0
j = 0
st = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
      '404': 0,'405': 0, '500': 0}

def display():
    """displays the result"""
    print("File size: {}".format(size))
    for k,v in sorted(st.items()):
        if v > 0:
            print("{:s}: {:d}".format(k, v))

try:
    for ln in stdin:
        list_ln = ln.split()
        if len(list_ln) >= 0:
            sta = list_ln[-2]
            size += int(list_ln[-1])
            if sta in st:
                st[sta] += 1
        j += 1
        if j % 10 == 0:
            display()
    display()
except KeyboardInterrupt as err:
    display()
