#!/usr/bin/python3

from urllib.request import urlopen
import sys

url = sys.argv[1]
request = urllib.request.Request(url)
if __name__ == "__main__":

    with urlopen("https://intranet.hbtn.io") as response:
        x-Request-Id = response.getheader('X-Request-Id')
        print(x_request_id)
