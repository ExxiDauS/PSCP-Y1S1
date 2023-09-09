"""Inflation"""

def year(price, year):
    'check for year'
    for _ in range(year):
        price += price * (3.81 / 100)
    check = str(price).find(".")
    print("%.2f" % float(str(price)[:check + 3]))

year(float(input()), int(input()))
