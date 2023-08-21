"""Circular I"""

def main():
    """Circular I"""
    numx = float(input())
    numy = float(input())
    numr = float(input())
    numxn = float(input())
    numyn = float(input())
    cal = ((numxn-numx)**2+(numyn-numy)**2)**0.5
    if cal <= numr:
        print("Yes")
    else:
        print("No")
main()
