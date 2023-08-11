"""Ball"""


def bounce(height):
    "ball"
    # centimeter
    height *= 100
    count = 0
    flag = False
    while flag == False:
        height = height * 0.6
        count += 1
        if height < 1:
            flag = True
            count -= 1
    print(count)


bounce(float(input()))
