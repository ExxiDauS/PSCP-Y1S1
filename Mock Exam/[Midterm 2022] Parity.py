"""[Midterm 2022] Parity"""

def parity(binary, odd_even):
    'using loop'
    find_1 = 0
    for check in str(binary):
        if check == "1":
            find_1 += 1
    if odd_even == "Odd":
        if find_1 % 2 == 0:
            print(str(binary) + "1")
        else:
            print(str(binary) + "0")
    elif odd_even == "Even":
        if find_1 % 2 == 0:
            print(str(binary) + "0")
        else:
            print(str(binary) + "1")

parity(str(input()), str(input()))
