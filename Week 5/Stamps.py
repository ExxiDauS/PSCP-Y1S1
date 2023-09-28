"""Stamps"""

def main():
    """Stair"""
    step = int(input())
    stair = int(input())
    sumkao = 0
    tmp = 0
    out = 0
    for _ in range(stair):
        heightstair = int(input())
        tmp = heightstair + tmp
        if heightstair > step:
            out = 1
        elif tmp == step:
            sumkao += 1
            tmp = 0
        elif tmp > step:
            sumkao += 1
            tmp = heightstair
    if tmp > 0:
        sumkao += 1
    if out == 1:
        print("NO")
    else:
        print(sumkao)
main()
