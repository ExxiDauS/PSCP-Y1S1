"""[Midterm 2021] ฉันจะเป็น Saitama ให้ได้เลย"""

def saitama(push_up, sit_up, sit_up02, jogging, p_per_d, s_per_d, s02_per_d, j_per_d):
    'exercise'
    push_day = push_up / p_per_d
    sit_day = sit_up / s_per_d
    sit02_day = sit_up02 / s02_per_d
    jogging_day = jogging / j_per_d
    check_seq = str(str(push_day) + " " + str(sit_day) + " " \
            + str(sit02_day) + " " + str(sit02_day)).split(" ")
    max_val = ""
    for item in check_seq:
        # Compare the current item with max_val
        if item > max_val:
            max_val = item

    print(max_val)

saitama(int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()))
