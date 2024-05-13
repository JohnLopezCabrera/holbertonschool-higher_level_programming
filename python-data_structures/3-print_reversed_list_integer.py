#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = my_list
    for x in range(len(a) - 1, -1, -1):
        print("{:d}".format(a[x]))
