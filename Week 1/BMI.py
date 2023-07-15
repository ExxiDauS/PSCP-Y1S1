"""BMI"""


def enterthedata():
    "data"
    name = str(input())
    kilogram = float(input())
    centimeter = float(input())
    somethung = kilogram / ((centimeter / 100) ** 2)
    print(name + "'s ", "BMI = ", end="")
    print("%.2f" % somethung)


enterthedata()
enterthedata()
enterthedata()
enterthedata()
enterthedata()
