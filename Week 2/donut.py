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


'''
    count = 0
    pay = 0
    check = 0
 
    while count < need:
        if count + promo + extra < need:
            count += promo + extra
            pay += price * promo
        else:
            pay += price
            check += 1
            count += 1
            if check == promo:
                count += extra
                check = 0
 
    return "%d %d" % (pay, count)
 
'''

'''
multi = need / promo + extra
pay += price * (promo * multi)
count += multi
if count < need:
    if need - count < promo:
        count += need - count
        pay += price * (need - count)
    else:
        count += promo + extra
        pay += price * promo
'''

'''
    count = 0
    pay = 0

    multi = need // (promo + extra)
    pay += price * (promo * multi)
    count += multi * (promo + extra)

    if count < need:
        if need - count < promo:
            count += need - count
            pay += price * (need - count)
        else:
            count += promo + extra
            pay += price * promo

    return "%d %d" % (pay, count)
'''
