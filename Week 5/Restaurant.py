"""Restaurant"""

def main():
    """RuleofThree"""
    size = int(input())
    price = float(input())
    sizekanom = float(input())
    raka = sizekanom/price
    tmp = raka
    tmpprice = price
    for _ in range(size-1):
        price = float(input())
        sizekanom = float(input())
        raka = sizekanom/price
        if raka > tmp:
            tmpprice = price
            tmp = raka
        elif raka == tmp:
            if price < tmpprice:
                tmpprice = price
                tmp = raka
        else:
            tmpprice = tmpprice
            tmp = tmp
    print("%.2f %.2f" %(tmpprice, tmp*tmpprice))
main()
