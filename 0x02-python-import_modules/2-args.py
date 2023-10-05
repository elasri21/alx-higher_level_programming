#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argv = argv[1:]
    length = len(argv)
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(1, argv[0]))
    else:
        print("{} arguments:".format(length))
        for i in range(0, length):
            print("{}: {}".format((i + 1), argv[i]))
