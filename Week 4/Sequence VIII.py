"""Sequence VIII"""


def seq8(number):
    "seq8"
    space = number
    starting = 1
    for _ in range(0, number):
        print(" " * (space * 2), end="")
        for counting in range(1, starting + 1):
            if counting == starting:
                print("%02d" % counting, end="")
            # elif:
            else:
                print("\b%02d" % counting, end=" ")
        print()
        space -= 1
        starting += 1


seq8(int(input()))
