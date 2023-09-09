"""[Recommend] Grade III"""

import math

def grade(subject):
    'avg check if'
    avg = 0
    for _ in range(subject):
        grader = float(input())
        if grader >= 95 and grader <= 100:
            avg += 4
        elif grader >= 90 and grader < 95:
            avg += 3.5
        elif grader >= 85 and grader < 90:
            avg += 3
        elif grader >= 80 and grader < 85:
            avg += 2.5
        elif grader >= 75 and grader < 80:
            avg += 2
        elif grader >= 70 and grader < 75:
            avg += 1.5
        elif grader >= 65 and grader < 70:
            avg += 1
        elif grader >= 60 and grader < 65:
            avg += 0.5
    print("%.2f" % ((math.floor((avg/subject)*100))/100))
grade(int(input()))
