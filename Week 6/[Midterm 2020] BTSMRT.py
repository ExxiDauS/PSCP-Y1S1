"""[Midterm 2020 + Recommend] BTSMRT"""

def btscheck(days, ages, height):
    'check days'
    if ages < 14 and height < 90:
        print("FREE")
    elif days == "Children Day" and ages < 14 and height <= 140:
        print("FREE")
    elif days == "Senior Day" and ages >= 60:
        print("FREE")
    else:
        print("PAY")
btscheck(str(input()), float(input()), float(input()))
