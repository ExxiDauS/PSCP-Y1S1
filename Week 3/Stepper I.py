"""Stepper I"""


def main(number):
    "step"
    startnum = 1
    for _ in range(0, number):
        print(startnum)
        startnum += 1


main(int(input()))
