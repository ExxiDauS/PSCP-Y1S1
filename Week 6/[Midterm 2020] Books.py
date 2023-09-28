"""Ejudge"""
import math
def main():
    """Books"""
    book = int(input())
    page = int(input())
    val_x = int(input())
    val_y = int(input())
    numpage = 0
    day = 0
    count = 0
    while True:
        calpage = math.ceil((val_x/val_y)*page)
        if book == count:
            break
        if calpage >= page:
            break
        numpage += calpage
        if numpage >= page:
            count += 1
            numpage = 0
        val_x += 1
        val_y += 1
        day += 1
    day += book-count
    print(day)
main()
