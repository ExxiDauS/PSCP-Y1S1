'''Build a bridge with your brick!'''

def brick(small, large, goal):

    '''Build a bridge with your brick!'''

    used = min(goal // 5, large)
    goal -= used * 5


    if small >= goal:
        return goal
    elif small < goal:
        return "-1"

print(brick(int(input()), int(input()), int(input())))
