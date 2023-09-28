"""Turnstile"""

def main():
    """Turnstile"""
    people = 0
    unlock = 0
    while True:
        act = input().upper()
        if act == "END":
            break
        if act == "C":
            unlock = 1
        if act == "P" and unlock == 1:
            people += 1
            unlock = 0
    print(people)
main()
