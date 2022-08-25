#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("{} arguments.".format(length))
    else:
        prefix = ''
        if length > 1:
            prefix = 's'
        print("{} argument{}:".format(length, prefix))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
