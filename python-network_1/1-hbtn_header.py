#!/usr/bin/python3
"""
Bu skript arqument kimi verilən URL-ə sorğu göndr
və cavab başlığındakı 'X-Request-Id' dəyərini çıxarır.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        # Dəyişən adında tire istifadə etmək olmaz, alt xətt (_) istifadə et.
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
