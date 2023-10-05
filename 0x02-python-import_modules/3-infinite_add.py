#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argv = argv[1:]
    result = 0
    for n in argv:
        result += int(n)
    print("{}".format(result))
