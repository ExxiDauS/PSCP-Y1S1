"""Weight Station"""
def main():
    """WeightStation"""
    avg = float(input())
    weight1 = float(input())
    weight2 = float(input())
    weight3 = float(input())
    avghalf = avg/2
    tmpw4 = (avg*4)-(weight1+weight2+weight3)
    if tmpw4+weight1+weight2+weight3 >= 15000:
        print("Overweight")
    elif abs(avg-weight1) >= avghalf or abs(avg-weight2) >= avghalf \
or abs(avg-weight3) >= avghalf or abs(avg-tmpw4) >= avghalf:
        print("Unbalance")
    else:
        print("Pass %.2f" %tmpw4)
main()
