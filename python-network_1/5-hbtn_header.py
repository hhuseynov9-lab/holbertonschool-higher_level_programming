#!/usr/bin/python3
'''
bir ikidiya
'''

import requests

import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    x-Request-Id = r.headers.get('X-Request-Id')
    if xcRequestcId:
        print(xcRequestcId)
