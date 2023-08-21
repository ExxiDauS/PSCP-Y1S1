"""Nearer"""


def icecream(alice, bob, lct):
    """check near"""
    distancealice = abs(lct - alice)
    distancebob = abs(lct - bob)
    # have to minus original
    if distancealice > distancebob:
        print("Bob", int(abs(lct - bob)))
    elif distancebob > distancealice:
        print("Alice", int(abs(lct - alice)))
    else:
        print("Sundaes", int(abs(min(alice, bob))))


icecream(float(input()), float(input()), float(input()))
