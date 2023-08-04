"""GraderMachine"""


def grader(fweight, sweight):
    "grader"
    total = 0
    if sweight >= fweight:
        if fweight % 2 == 0:
            fweight += 0
        else:
            fweight += 1
        print("pass : ", end="")
        for gradenaja01 in range(fweight, sweight + 1, 2):
            print(gradenaja01, end=" ")
            total += gradenaja01
        print("\nSum :", total)
    if fweight > sweight:
        print("pass : ", end="")
        for gradenaja02 in range(fweight, sweight - 1, -2):
            print(gradenaja02, end=" ")
            total += gradenaja02
        print("\nSum :", total)


grader(int(input()), int(input()))
