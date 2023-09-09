"""Key"""

def key(identity):
    "id check"
    total = 0
    for number in identity:
        total += int(number)
    total += int(identity[10:13]) * 10
    if total < 1000:
        total += 1000
    total = str(total)
    print(total[-4:])
key(str(input()))
