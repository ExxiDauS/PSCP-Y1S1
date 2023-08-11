"""Left Arrow"""


def main(first_num, second_num):
    "Left arrow"
    space = second_num // 2
    for _ in range(0, second_num):
        print(" " * abs(space), end="")
        print("*" * first_num)
        space -= 1


main(int(input()), int(input()))
