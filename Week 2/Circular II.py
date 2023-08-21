"""Circular II"""

def main():
    """Circular II"""
    numx = float(input())
    numy = float(input())
    numr = float(input())
    numxf = float(input())
    numyf = float(input())
    numrf = float(input())
    cal = ((numxf-numx)**2+(numyf-numy)**2)**0.5
    if cal < numr+numrf:
        print("Yes")
    else:
        print("No")
main()
