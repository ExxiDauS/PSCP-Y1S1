"""Boomerang"""
import math
def main(xxx, yyy, zzz):
    'docnaja'
    ex01 = xxx + 1
    ex02 = 7*(yyy**3) + 2*(yyy**2) - (31*yyy) + 1
    ex03 = -zzz
    ex04 = (xxx + yyy) * (xxx - yyy)
    ex05 = ((yyy - (math.sqrt((yyy**2)-(4*xxx*zzz))))/(2*xxx))
    print(ex01, ex02, ex03, ex04, ex05, sep="\n")
main(int(input()), int(input()), int(input()))
