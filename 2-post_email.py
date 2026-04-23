#!/usr/bin/python3

'''
decode team
'''

from urllib.request import urlopen
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email":sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    with urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
