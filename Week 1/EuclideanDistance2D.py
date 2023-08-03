"""EuclideanDistance2D"""


def main(qq1, qq2, pp1, pp2):
    "calculator"
    import math

    print(math.sqrt(((qq1 - pp1) ** 2) + ((qq2 - pp2) ** 2)))


main(float(input()), float(input()), float(input()), float(input()))
