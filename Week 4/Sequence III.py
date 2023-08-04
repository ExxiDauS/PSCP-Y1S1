"""Sequence III"""


def seq3(number):
    "seq3"
    starting = 2
    for _ in range(0, number):
        for counting in range(starting, number + starting):
            print(counting, end=" ")
        print("")
        starting += 1


seq3(int(input()))
