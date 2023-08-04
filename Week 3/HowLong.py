"""HowLong"""


def checklong(number):
    "len without len"
    nubnaja = 0
    for _ in str(abs(number)):
        nubnaja += 1
    print(nubnaja)


checklong(int(input()))
