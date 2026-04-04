#!/usr/bin/python3

import sys

'''
infinity adding
'''
if __name__ == "__main__":
    total = 0
    for num in sys.argv[1:]:
        total = total + num
    print(total)
