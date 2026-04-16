#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            counter += 1
            print("{:d}".format(my_list[i]), end="")
        except (IndexError, ValueError):
            continue
    print("{:d}".format(counter))
