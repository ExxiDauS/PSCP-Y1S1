"""Brick Bridge"""


def bridge(small_brick, large_brick, goal):
    "build the bridge"
    goal_01 = goal - (large_brick * 5)
    count = 0
    if (small_brick + (large_brick * 5)) < goal:
        print("-1")
    else:
        #abs?
        goal -= (large_brick * 5)
        if goal_01 < 0:
            while goal_01 < goal:
                goal_01 += 5
            goal_01 -= 5
            for _ in range(small_brick):
                goal_01 += 1
                count += 1
                if goal_01 == goal:
                    break
            print(count)
        else:
            print(goal)

bridge(int(input()), int(input()), int(input()))
