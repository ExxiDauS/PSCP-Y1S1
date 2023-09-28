"""Align"""

import math

def main():
    """Align"""
    size = int(input())
    align = input().lower()
    txt = input()
    cal = size-len(txt)
    if align == "left":
        if len(txt) > size:
            print(txt[:size])
        else:
            print(txt)
    elif align == "center":
        left = math.ceil(cal/2)
        right = math.floor(cal/2)
        print(" "*left+ txt +" "*right)
    elif align == "right":
        if len(txt) > size:
            print(txt[:size])
        else:
            print(txt.rjust(size))
main()
