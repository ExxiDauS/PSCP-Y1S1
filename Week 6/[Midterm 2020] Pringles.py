"""Ejudge"""
def main():
    """Pringles"""
    canup = input()
    chip = input()
    candown = input()
    finger = int(input())
    eatchip = chip[:finger]
    chipincan = chip[finger:]
    chipcount = 0
    incan = 0
    for i in eatchip:
        if i == ")":
            chipcount += 1
    for i in chipincan:
        if i == ")":
            incan += 1
    print(chipcount)
    if incan == 0:
        print("None.")
    else:
        print("There are still some left.")
    print(canup)
    print(" "*finger+chipincan)
    print(candown)
main()
