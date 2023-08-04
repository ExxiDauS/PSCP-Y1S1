"""Stepper II"""


def main(number01, number02):
    "loop num"
    if number01 > number02:
        for starting in range(number01, number02 - 1, -1):
            print(starting)
    elif number02 > number01:
        for anotherstart in range(number01, number02 + 1, 1):
            print(anotherstart)
    elif number01 == number02:
        print(number01)


main(int(input()), int(input()))
