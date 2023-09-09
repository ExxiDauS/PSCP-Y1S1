"""Hello"""
def calculate(high, amount, error):
    """work"""
    default = high
    count = 0
    while amount:
        high -= int(input())
        if high < 0:
            error = 1
        elif high == 0:
            high = default
            count += 1
        amount -= 1
    if high != default:
        count += 1
    if error:
        print("NO")
    else:
        print(count)
calculate(int(input()), int(input()), 0)
