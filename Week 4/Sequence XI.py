"""Sequence XI"""

def main():
    """Sequence XI"""
    line = int(input())
    for i in range(-line + 1, line, 1):
        for j in range(-line + 1, line, 1):
            if abs(i) > abs(j) - 1:
                print("%02d" %(line - abs(i)), end=" ")
            else:
                print("%02d" %(line - abs(j)), end=" ")
        print()
main()
