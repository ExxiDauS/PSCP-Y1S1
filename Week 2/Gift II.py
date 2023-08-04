"""Gift II"""


def checkna(countnaja, printnum):
    "gift"
    if countnaja > 0:
        weight = int(input())
        if weight % 2 == 0:
            printnum = weight
    else:
        print(printnum)
        return
    checkna(countnaja - 1, printnum)


def main():
    "counting"
    number = 0
    checkna(8, number)


main()
