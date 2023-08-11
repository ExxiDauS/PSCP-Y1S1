"""Bill"""


def price(bill):
    "price"
    serv = (10 / 100) * bill
    if serv < 50:
        serv = 50
    elif serv >= 1000:
        serv = 1000
    total = bill + serv
    print("%.2f" % (total + ((7 / 100) * total)))


price(float(input()))
