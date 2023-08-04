"""Day I"""


def year(christ):
    "yearnaja"
    ryear = christ % 4
    if christ % 100 == 0 and christ % 400 != 0:
        print("No")
    else:
        print("Yes" if ryear == 0 else "No")


year(float(input()))
