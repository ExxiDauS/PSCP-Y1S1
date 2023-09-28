"""Ejudge"""
def main():
    """Donut"""
    price = int(input())
    buy = int(input())
    free = int(input())
    minwant = int(input())
    donut = 0
    pro = buy+free
    buypro = minwant // pro
    if minwant == 0:
        print("0 0")
    if minwant > 0:
        donut = pro * buypro
        left = minwant - donut
        if left > buy:
            left = buy
        if left >= buy:
            donut += pro
        else:
            donut += left
        print("%d %d" %((price*buypro*buy)+(left*price), donut))
main()
