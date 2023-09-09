"""LastStand"""

import json

def laststand(txt):
    'using json to help'
    txt = json.loads(txt)
    txt = list(map(str, txt))
    for num in txt:
        print(num[-1])
laststand(input())
