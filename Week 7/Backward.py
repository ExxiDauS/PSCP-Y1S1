"""Backward"""

def back():
    'list 01'
    txt = []
    flag = True
    while flag == True:
        input_txt = input()
        if input_txt == "NULL":
            flag = False
        else:
            txt.append(input_txt)
    txt.reverse()
    for aws in txt:
        print(aws)
back()
