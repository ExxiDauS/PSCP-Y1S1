"""Sequence IV"""


def seq4(number):
    "seq4"
    starting = 1
    for _ in range(0, number):
        for counting in range(starting, number + starting):
            print(counting, end=" ")
        print("")
        starting += number


seq4(int(input()))
