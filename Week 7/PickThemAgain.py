"""PickThemAgain"""

def pickag(txt):
    'pick %3 or %5'
    count = 0
    txt = str(txt).split()
    txt = list(map(int, txt))
    txt.reverse()
    for num in txt:
        if num % 3 == 0 or num % 5 == 0:
            print(num)
            count += 1
    if count == 0:
        print("Nope")
pickag(input())
