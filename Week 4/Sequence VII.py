"""Sequence VII"""


def seq7(number):
    "seq7"
    starting = 1
    for _ in range(0, number):
        for counting in range(1, starting + 1):
            print(counting, end=" ")
        print("")
        starting += 1
    for _ in range(0, number):
        for recounting in range(1, starting - 1):
            print(recounting, end=" ")
        print("")
        starting -= 1


seq7(int(input()))
