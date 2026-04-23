#!/usr/bin/python3
"""
Bu skript HTTP xətalarını idarə edərək URL-dən məlumat çəkir.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Sorğunu göndəririk
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    
    except urllib.error.HTTPError as e:
        # Əgər 404, 403 kimi HTTP xətası baş verərsə
        print("Error code: {}".format(e.code))
