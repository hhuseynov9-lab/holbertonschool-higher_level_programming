#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}

    # Datatnı hazırlayırıq (urlencode) və bayta çeviririk (encode)
    data = urllib.parse.urlencode(payload).encode('utf-8')

    # Request obyektini yaradırıq
    req = urllib.request.Request(url, data=data)

    # Sorğunu göndərib cavabı oxuyuruq və decode edirik
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
