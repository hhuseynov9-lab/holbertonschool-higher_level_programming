#!/usr/bin/python3
def uppercase(str):
    for chc in str:
        code = ord(chc)
        if code >= 97 and code <= 122:
            chc = chr(ord(chc) - 32)
        print("{}".format(chc), end="")
    print()
