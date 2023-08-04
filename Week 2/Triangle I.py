"""Triangle I"""


def triangle(number_01, number_02, number_03):
    "trigone"
    # check = (number_03**2) == ((number_01**2) + (number_02**2))
    # print("Yes" if check == True else "No")
    checknumber = (number_01**2) + (number_02**2)
    result = number_03**2
    if checknumber != result:
        checknumber += 0.01
        if checknumber == result:
            print("Yes")
        elif checknumber != result:
            checknumber -= 0.02
            print("Yes" if checknumber == result else "No")
    else:
        print("Yes" if checknumber == result else "No")


triangle(float(input()), float(input()), float(input()))
