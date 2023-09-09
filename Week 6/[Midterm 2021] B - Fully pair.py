"""[Midterm 2021] B - Fully pair?"""

def pair(pairname):
    "string loop"
    no_pair = ""
    for check in pairname:
        alphafind = str(pairname).count(check)
        check_same = no_pair.count(check)
        if alphafind % 2 != 0:
            if check_same == 0:
                no_pair += str(check)
            else:
                pass
    if no_pair == "":
        print("fully paired")
    else:
        print(no_pair)

pair(str(input()))
