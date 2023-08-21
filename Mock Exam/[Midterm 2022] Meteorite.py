"""[Midterm 2022] Meteorite"""

def meteorite(weight, amount, danger):
    'check amount'
    meteor = 1
    missile = 0
    while weight >= danger:
        missile += meteor
        weight = (weight / amount)
        meteor = (amount * meteor)
    print(int(missile))

meteorite(float(input()), float(input()), float(input()))
