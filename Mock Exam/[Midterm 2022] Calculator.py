"""[Midterm 2022] Calculator"""

def calculator(number):
    'while check'
    flag = False
    amount = 0
    press_num = 1
    while flag == False:
        for _ in str(press_num):
            amount += 1
        amount += 1
        press_num += 1
        if press_num > number:
            flag = True
    print(amount if number != 1 else "1")

calculator(int(input()))
