#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    y = my_list
    for x in range(len(y) - 1, -1, -1):
        print("{:d}".format(y[x]))
