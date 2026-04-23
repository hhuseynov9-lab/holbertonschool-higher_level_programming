#!/usr/bin/python3
"""
Bu skript verilən URL-ə email parametri ilə POST sorğusu göndərir
və cavabın body hissəsini utf-8 formatında çap edir.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    
    # 1. Datatnı URL-encoded formata salırıq və baytlara (bytes) çeviririk
    data = urllib.parse.urlencode(values).encode('utf-8')
    
    # 2. Request obyektini yaradırıq (data əlavə etdiyimiz üçün avtomatik POST olur)
    req = urllib.request.Request(url, data=data)
    
    # 3. Sorğunu göndəririk və cavabı oxuyuruq
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
