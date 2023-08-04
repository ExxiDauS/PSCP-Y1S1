"""SumOfNumber"""


def sumnaja(goal):
    "sum"
    summary = 0
    flag = False
    while summary != goal or flag == True:
        number = int(input())
        if number != -1:
            summary += number
        else:
            flag = True
            print(summary)
            break
    if summary == goal:
        print(summary)


sumnaja(int(input()))
