"""Point in Circle"""


def circle(xxx, yyy, xxn, yyn, rrr):
    "fk math"
    distance = ((xxn - xxx) ** 2) + (((yyn - yyy) ** 2))
    if distance <= rrr**2 or distance == 0:
        print(True)
    else:
        print(False)


circle(float(input()), float(input()), float(input()), float(input()), float(input()))
