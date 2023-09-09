"""Hamburger"""

def main(first_bun, second_bun):
    'Hamberger'
    print("|" * first_bun + "*" * ((first_bun + second_bun)*2) + "|" * second_bun)
main(int(input()), int(input()))
