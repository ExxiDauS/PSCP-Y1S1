"""[Midterm 2020] Phone Number"""

def phone(phonenum, checkinter):
    'international'
    count_in_loop = 0
    if len(phonenum) == 9:
        if checkinter == "Domestic":
            for countcheck in phonenum:
                if count_in_loop % 4 == 0:
                    print(countcheck, end=" " )
                else:
                    print(countcheck, end="")
                count_in_loop += 1
        if checkinter == "International":
            for countcheck in phonenum:
                if count_in_loop % 4 == 0:
                    print(countcheck, end=" ")
                else:
                    print(countcheck, end="")
                count_in_loop += 1
    elif len(phonenum) == 10:
        if checkinter == "Domestic":
            for countcheck in phonenum:
                if count_in_loop == 0:
                    print(countcheck, end="")
                elif count_in_loop == 1:
                    print(countcheck, end=" ")
                elif count_in_loop % 5 == 0:
                    print(countcheck, end=" ")
                else:
                    print(countcheck, end="")
                count_in_loop += 1
        if checkinter == "International":
            for countcheck in phonenum:
                if count_in_loop == 0:
                    print("+66", end="")
                elif count_in_loop == 1:
                    print(countcheck, end=" ")
                elif count_in_loop % 5 == 0:
                    print(countcheck, end=" ")
                else:
                    print(countcheck, end="")
                count_in_loop += 1
                
phone(str(input()), str(input()))
