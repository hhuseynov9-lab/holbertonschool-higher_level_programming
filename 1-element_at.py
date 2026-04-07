#!/usr/bin/pyhton3
def element_at(my_list, idx):
    if idx < 0 and idx != 0:
        print("None")
    if idx > len(my_list):
        print("None")
    else:
        print(print("Element at index {:d} is {}".format(idx, element_at(my_list, idx))))
