#!/usr/bin/python3

'''
bir ikidya ciqida
'''

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = request.get(url)
    if r.status >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
