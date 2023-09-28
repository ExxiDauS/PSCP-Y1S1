"""Ejudge"""
import math
def main():
    """saitama"""
    pushupwant = int(input())
    situpwant = int(input())
    lukwant = int(input())
    runwant = int(input())
    pushupday = int(input())
    situpday = int(input())
    runday = int(input())
    lukday = int(input())
    pushup = pushupwant/pushupday
    situp = situpwant/situpday
    run = runwant/runday
    luk = lukwant/lukday
    if pushup > situp:
        tmp1 = pushup
    else:
        tmp1 = situp
    if luk > run:
        tmp2 = luk
    else:
        tmp2 = run
    if tmp1 > tmp2:
        print(math.ceil(tmp1))
    else:
        print(math.ceil(tmp2))
main()
