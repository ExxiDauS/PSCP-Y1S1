"""BootSequence"""


def bootseq(number):
    "seq"
    for sequence in range(1, number + 1):
        print(sequence, end="")
        if sequence != number:
            print("", end="_")


bootseq(int(input()))
