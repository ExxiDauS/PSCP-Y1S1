"""Frame"""


def frame(msg):
    "frame"
    space = len(str(msg)) + 2
    print("*" * space, "*" + msg + "*", "*" * space, sep="\n")


frame(input())
