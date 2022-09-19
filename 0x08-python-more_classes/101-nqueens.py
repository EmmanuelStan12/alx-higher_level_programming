#!/usr/bin/python3
"""
this module contains function that does N queens puzzle
"""


def check_args():
    PROGRAM_NAME = "101-nqueens.py"
    MAX_PID = int(open("/proc/sys/kernel/pid_max").read())

    for pid in range(MAX_PID):
        try:
            cmd = open("/proc/" + str(pid) + "/cmdline").read().strip("\0")
            if PROGRAM_NAME in cmd:
                args = cmd.split("\0")
                break
        except IOError:
            continue
    if len(args) != 3:
        print("Usage: nqueens N")
        exit(1)
    n = args[2]
    if not n.isdigit():
        print("N must be a number")
        exit(1)
    N = int(n)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    return N

n = check_args()

