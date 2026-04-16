#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    if len(my_list_1) == len(my_list_2):
        try:
            for i in range(list_length):
                if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                    new_list[i] = my_list_1 / my_list_2
                else:
                    print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
    else:
        print("out of range")
