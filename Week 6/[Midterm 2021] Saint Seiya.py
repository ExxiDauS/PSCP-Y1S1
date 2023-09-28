"""Ejudge"""
def main():
    """Saint Seiya"""
    second = int(input())
    punchkamnod = int(input())
    punch = 0
    for i in range(2, second+1, 2):
        if punch < punchkamnod:
            if i % 6 == 0:
                punch += 1
            elif i % 2 == 0:
                punch += 165
        else:
            punch += (second+1-i)*12
            break
    print(punch)
main()
