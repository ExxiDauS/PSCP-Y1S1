"""Align"""

def align(size, alignment, txt):
    'align text'
    if alignment == "left":
        print(str(txt).ljust(size))
    elif alignment == "center":
        print(str(txt).center(size))
    elif alignment == "right":
        print(str(txt).rjust(size))
align(int(input()), str(input()), str(input()))
