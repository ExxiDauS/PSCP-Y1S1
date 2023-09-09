"""ValidVar"""

def validcheck(number):
    'identify check'
    reserved_check = "if else elif while for True False continue break\
                    return is in and or from as pass not def None"
    for _ in range(number):
        variable = str(input())
        if str(variable).isidentifier() == False or variable in reserved_check.split(" "):
            print("Invalid")
        else:
            print("Valid")

validcheck(int(input()))
