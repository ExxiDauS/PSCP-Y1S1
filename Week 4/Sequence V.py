"""Sequence V"""


def seq5(number):
    "seq5 with 7"
    countfor7 = 0
    for counting in range(number, 0, -1):
        print(counting, end=" ")
        countfor7 += 1
        if countfor7 == 7:
            print("")
            countfor7 = 0


seq5(int(input()))
