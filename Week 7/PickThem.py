"""PickThem"""

import json

def even(txt):
    'some loop check'
    txt = json.loads(txt)
    count = 0
    for num in txt:
        if num % 2 == 0:
            print(num)
            count += 1
    if count == 0:
        print("Nope")
even(input())
