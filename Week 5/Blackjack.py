"""Blackjack"""

def main():
    """Blackjack"""
    many = int(input())
    total = 0
    wtf_a = 0
    if many > 0 and many <= 3:
        for _ in range(0, many):
            point = input().upper()
            if point == "J" or point == "Q" or point == "K":
                total += 10
            elif point.isnumeric() and int(point) > 1 and int(point) < 11:
                total += int(point)
            elif point == "A":
                total += 11
                wtf_a += 1
        while total > 21 and wtf_a > 0:
            total -= 10
            wtf_a -= 1
    print(total)
main()
