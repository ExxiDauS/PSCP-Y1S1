"""[Midterm 2022] Coke"""

def coke(price, bottlecap, new_price, require):
    'donut but coke'
    if bottlecap == 0:
        pay = price * require
        #case 0
    elif require == 0:
        pay = 0
    else:
        trade_bottle = require // bottlecap
        if require % bottlecap == 0:
            trade_bottle -= 1
        require -= trade_bottle
        pay = (price * require) + (trade_bottle * new_price)
    print(int(pay))
coke(float(input()), float(input()), float(input()), float(input()))
