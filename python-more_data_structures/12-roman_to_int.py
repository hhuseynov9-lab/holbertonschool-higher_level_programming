#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    c = []
    cem = 0
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    for s in roman_string:
        for key, value in roman_values.items():
            if s == key:
                c.append(value)
    if len(c) == 0:
        return 0
    for i in range(len(c) - 1):
        if c[i] >= c[i+1]:
            cem = cem + c[i]
        else:
            cem = cem - c[i]
    cem = cem + c[-1]

    return cem
