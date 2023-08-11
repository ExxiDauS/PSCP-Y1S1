"""Key"""


def key(identity):
    "id check"
    lst = []
    lstforkey = []
    total = 0
    counting = 13
    for number in identity:
        lst.append(int(number))
        total += int(number) * counting
        counting -= 1
    keycheck = total + (lst[-3] * 10) + (lst[-2] * 10) + (lst[-1] * 10)
    if keycheck > 9999:
        keycheck %= 10000
    elif keycheck <= 999:
        keycheck += 1000
    print(keycheck)


key(input())
