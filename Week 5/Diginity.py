"""Diginity"""

def main():
    """Diginity"""
    while True:
        num = input()
        if num == "0":
            break
        while len(num) > 1:
            num = str(sum([int(i) for i in num]))
        print(num)
main()
