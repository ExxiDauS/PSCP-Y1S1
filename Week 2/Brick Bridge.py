"""Brick Bridge"""


def bridge(small_brick, large_brick, goal):
    "build the bridge"
    rangenaja = 0
    if rangenaja < goal:
        rangenaja += large_brick * 5
        while rangenaja > goal:
            rangenaja -= 5
    small_brick_use = abs(rangenaja - goal)
    if rangenaja < goal:
        rangenaja += small_brick_use
    print(small_brick_use if rangenaja == goal else "-1")


bridge(int(input()), int(input()), int(input()))
