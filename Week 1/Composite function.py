"""Composite Function"""


def main(number):
    "function"
    fgx = 2 * ((number / 2) + 1)
    gfx = ((2 * number) / 2) + 1
    print("%.2f" % fgx)
    print("%.2f" % gfx)


main(int(input()))
