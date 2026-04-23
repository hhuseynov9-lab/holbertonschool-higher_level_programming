#!/usr/bin/python3
"""
Uses GitHub API to display the user id using Basic Authentication.
"""
import requests
import sys


if __name__ == "__main__":
    # Terminaldan istifadəçi adı və tokeni götürürük
    username = sys.argv[1]
    password = sys.argv[2]

    # GitHub API-nin istifadəçi məlumatları üçün olan endpointi
    url = "https://api.github.com/user"

    # Basic Authentication istifadə edərək GET sorğusu göndəririk
    r = requests.get(url, auth=(username, password))

    try:
        # Cavabı JSON formatına çeviririk
        user_data = r.json()

        # İstifadəçinin ID-sini çap edirik
        # .get() istifadə edirik ki, əgər ID yoxdursa xəta verməsin
        print(user_data.get('id'))
    except ValueError:
        # Əgər cavab düzgün JSON deyilsə (çox nadir halda)
        pass
