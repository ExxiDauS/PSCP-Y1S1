"""Sequence I"""


def reboot(line):
    """reboot in line"""
    for _ in range(0, line):
        for numberinreboot in range(1, line + 1):
            print(numberinreboot, end=" ")
        print("")


reboot(int(input()))
