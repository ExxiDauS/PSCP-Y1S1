"""Nearer"""

def main():
    """Nearer"""
    alice = int(input())
    bob = int(input())
    ice = int(input())
    if abs(alice - ice) < abs(bob - ice):
        print("Alice", abs(alice - ice))
    elif abs(alice - ice) > abs(bob - ice):
        print("Bob", abs(bob - ice))
    else:
        print("Sundaes", abs(alice - ice))
main()
