"""Ejudge"""
def main():
    """iPhone 13 Again"""
    model = input().lower()
    size = input()
    price = 0
    if model == "iphone 13 mini":
        price += 25900
    elif model == "iphone 13":
        price += 29900
    elif model == "iphone 13 pro":
        price += 38900
    elif model == "iphone 13 pro max":
        price += 42900
    else:
        model = True
    if size == "128 GB":
        price += 0
    elif size == "256 GB":
        price += 4000
    elif size == "512 GB":
        price += 12000
    elif size == "1 TB" and (model == "iphone 13 pro" or model == "iphone 13 pro max"):
        price += 20000
    else:
        price = True
    if price == True or model == True:
        print("Not Available")
    else:
        print(price)
main()
