"""Donut"""
import math


def donut(price, buy, free, want):
    "donut"
    roundnaja = math.ceil(want / (buy + free))
    freepiece = roundnaja * free
    amtdonut = roundnaja * (buy + free)
    payprice = 0
    # if amtdonut > want and :
    #     amtdonut -= buy + free
    #     while amtdonut < want:
    #         payprice += price
    #         amtdonut += 1
    payprice = (amtdonut - freepiece) * price
    print(payprice, amtdonut)


donut(int(input()), int(input()), int(input()), int(input()))
