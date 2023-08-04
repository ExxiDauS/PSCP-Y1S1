"""DataSpike"""


def highdata(countnaja, highestnum):
    "check"
    if countnaja > 0:
        # input check
        number02 = int(input())
        # check
        if number02 > highestnum:
            highestnum = number02
    else:
        print(highestnum)
        return
    highdata(countnaja - 1, highestnum)


def main():
    "run the program"
    number01 = 0
    highdata(8, number01)


main()
