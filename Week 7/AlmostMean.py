"""AlmostMean"""

def mean(people):
    'copy list'
    lst = []
    score = []
    for _ in range(people):
        information = input()
        information = information.split()
        lst.extend(information)
    student_id = lst[::2]
    for txt in lst:
        if txt in student_id:
            pass
        else:
            score.append(txt)
    print(student_id, score)
mean(int(input()))
