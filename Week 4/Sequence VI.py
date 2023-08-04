"""Sequence VI"""


def seq6(number):
    "seq6"
    starting = 1
    for _ in range(0, number):
        for counting in range(1, starting + 1):
            print(counting, end=" ")
        print("")
        starting += 1


seq6(int(input()))
