"""Future Message"""


def check_futuremsg(msg):
    "msg"
    if str(msg).isnumeric():
        print("Number")
    elif str(msg).isupper():
        print("Uppercase")
    elif str(msg).islower():
        print("Lowercase")
    elif str(msg).istitle():
        print("Title")
    elif str(msg).isspace():
        print("Space")
    else:
        print("Other")


check_futuremsg(input())
