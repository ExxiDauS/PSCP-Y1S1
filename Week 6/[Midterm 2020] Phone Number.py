"""[Midterm 2020] Phone Number"""

def phone(phonenum, checkinter):
    'international'
    if len(phonenum) == 9:
        if checkinter == "Domestic":
            #0 1234 4567
            print(phonenum[0], phonenum[1:5], phonenum[5:9])
        if checkinter == "International":
            print('+66', phonenum[1:5], phonenum[5:9])
    elif len(phonenum) == 10:
        if checkinter == "Domestic":
            #08 1234 5678
            print(phonenum[0:2], phonenum[2:6], phonenum[6:10])
        if checkinter == "International":
            print('+66'+phonenum[1:2], phonenum[2:6], phonenum[6:10])
phone(str(input()), str(input()))
