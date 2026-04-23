#!/usr/bin/python3
"""
Sends a POST request with a letter as a parameter to search for a user.
"""
import requests
import sys


if __name__ == "__main__":
    # Əgər arqument verilməyibsə q = "", əks halda verilən arqument
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        # POST sorğusu göndəririk
        r = requests.post(url, data=payload)
        
        # Cavabı JSON formatına çevirməyə çalışırıq
        result = r.json()

        # Əgər JSON boşdursa (məsələn: {})
        if not result:
            print("No result")
        else:
            # Tapılan istifadəçinin id və name dəyərlərini çap edirik
            print("[{}] {}".format(result.get('id'), result.get('name')))

    except ValueError:
        # Əgər cavab düzgün JSON formatında deyilsə (məsələn: adi text-dirsə)
        print("Not a valid JSON")
