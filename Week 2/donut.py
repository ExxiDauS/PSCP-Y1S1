'''le donut'''

def donut(price, promo, extra, need):

    '''le donut'''

    count = 0
    pay = 0

    multi = need // (promo + extra)
    pay += price * (promo * multi)
    count += multi * (promo + extra)

    if need > 0:
        left = need - count
        if left >= promo:
            left = promo
            count += promo + extra
        else:
            count += left
        pay += price * left

    return "%d %d" % (pay, count)

print(donut(int(input()), int(input()), int(input()), int(input())))
