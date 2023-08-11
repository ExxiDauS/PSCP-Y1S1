"""FOR!F-Ball"""


def magic(switch):
    "case"
    ball_locat = 1
    for check in switch:
        if check == "A" and ball_locat == 1:
            ball_locat += 1
        elif check == "A" and ball_locat == 2:
            ball_locat -= 1
        # elif check == "A" and ball_locat > 1:
        #     continue
        elif check == "B" and ball_locat == 2:
            ball_locat += 1
        elif check == "B" and ball_locat == 3:
            ball_locat -= 1
        # elif check == "B" and ball_locat == 1
        elif check == "C" and ball_locat == 3:
            ball_locat -= 2
        elif check == "C" and ball_locat == 1:
            ball_locat += 2
        else:
            continue
    print(ball_locat)


magic(input())
