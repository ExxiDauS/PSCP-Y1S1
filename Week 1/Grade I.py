"""Grade I"""


def main(score):
    "grade"
    if score < 0 and score > 100:
        return
    else:
        print("Pass" if score >= 60 else "Fail")


main(float(input()))
