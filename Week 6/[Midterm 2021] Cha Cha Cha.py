"""[Recommend + Midterm 2021] Cha Cha Cha"""

import math

def moneycal(days):
    'calculate money'
    if days > 31:
        return
    work_hours = 0
    for _ in range(days):
        work = math.ceil(float(input()))
        if work > 24:
            work_hours += 0
        else:
            work_hours += work
    print(int(work_hours * 8720))

moneycal(int(input()))
