#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        div = 0
        try:
            val1 = my_list_1[i]
            val2 = my_list_2[i]
            div_result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("division by 0")
        finally:
            new_list.append(div_result)
    return new_list
