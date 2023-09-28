"""Ejudge"""
def main():
    """diamond"""
    size = int(input())
    halfsize = size//2
    for i in range(size):
        for j in range(size):
            if i == halfsize or i+j == halfsize or \
                j-i == halfsize or j == size-i+halfsize-1 or i-j == halfsize:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()
