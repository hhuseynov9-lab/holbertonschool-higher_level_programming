#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    a1 = my_list[0]
    for i in range(1, len(my_list)):
        if a1 < my_list[i]:
            a1 = my_list[i]
    return a1
