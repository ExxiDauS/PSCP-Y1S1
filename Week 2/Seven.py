"""Seven"""


def expo(number):
    "expo"
    times = number % 4
    if times == 1:
        print("7")
    elif times == 2:
        print("9")
    elif times == 3:
        print("3")
    elif times == 4 or times == 0:
        print("1")


expo(float(input()))
