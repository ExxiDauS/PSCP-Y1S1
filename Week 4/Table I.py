"""Table I"""

def multi(number):
    'count'
    step = 1
    for _ in range(0, number):
        print("15 x", step, "=", 15 * step)
        step += 1
multi(int(input()))
