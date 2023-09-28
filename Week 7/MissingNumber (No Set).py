"""MissingNumber (No Set)"""

def missingnum(amount):
    'loop with list'
    num_check = []
    num = []
    for i in range(amount + 1):
        num_check.append(i)
    for _ in range(amount):
        enter_num = int(input())
        num.append(enter_num)
        if enter_num == 0:
            break
    for j in num:
        if j in num:
            num_check.remove(j)
    for aws in num_check:
        print(aws)
missingnum(int(input()))
