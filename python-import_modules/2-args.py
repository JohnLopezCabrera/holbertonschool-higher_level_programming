#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    args = sys.argv[1:]

    print("Number of argument(s):", end=" ")

    if num_args == 0:
        print(".", end="\n\n")
    elif num_args == 1:
        print("argument:", end="\n\n")
    else:
        print("arguments:", end="\n\n")

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
