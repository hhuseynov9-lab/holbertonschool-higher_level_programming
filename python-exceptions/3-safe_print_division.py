#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("bolunmur 0 a")
    finally:
        print("Inside result: {}".format(result))
