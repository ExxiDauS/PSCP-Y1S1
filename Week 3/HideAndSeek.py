"""HideAndSeek"""


def hideandseek(number01, number02, counting):
    "test argument"
    for numberofcount in range(number01, number02, counting):
        print(numberofcount)


hideandseek(int(input()), int(input()), int(input()))
