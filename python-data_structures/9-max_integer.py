#!/usr/bin/python3
def max_integer(my_list=[]):
    a1 = my_list[0]
    for i in range(len(1:my_list)):
        if a1 < my_list[i]:
            a1 = my_list[i]
    return a1
