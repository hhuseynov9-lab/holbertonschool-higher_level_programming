#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) != 0:
        max1 =  max(a_dictionary.values())
        for i in a_dictionary:
            if a_dictionary[i] == max1:
                print("{}".format(i))

    else:
        return None
