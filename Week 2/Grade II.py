"""Grade II"""


def main(grade):
    "love u"
    if grade >= 95 and grade <= 100:
        print("A")
    elif grade >= 90 and grade < 95:
        print("B+")
    elif grade >= 85 and grade < 90:
        print("B")
    elif grade >= 80 and grade < 85:
        print("C+")
    elif grade >= 75 and grade < 80:
        print("C")
    elif grade >= 70 and grade < 75:
        print("D+")
    elif grade >= 65 and grade < 70:
        print("D")
    elif grade >= 60 and grade < 65:
        print("F+")
    elif grade >= 0 and grade < 60:
        print("F")
    else:
        print("ERR")


main(float(input()))
