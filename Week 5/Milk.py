"""Milk"""

def main():
    """Milk"""
    price = int(input())
    pro = int(input())
    changemilk = int(input())
    money = int(input())
    milk = money // price
    tmp = milk
    while tmp >= pro and changemilk != 0:
        if pro == 0:
            break
        milk += changemilk
        tmp += changemilk
        tmp -= pro
    print(milk)
main()
