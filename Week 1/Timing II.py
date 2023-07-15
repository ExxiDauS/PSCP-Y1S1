"""Timing II"""


def main():
    "var test"
    second = int(input())
    minutes = second // 60
    second = second % 60
    hours = minutes // 60
    minutes = minutes % 60
    days = hours // 24
    hours = hours % 24
    print(
        "%04d:%02d:%02d:%02d" % (days, hours, minutes, second)
        if days < 10000
        else "ERR_:__:__:__"
    )


main()
