"""Virus I"""

def virus(virusbody):
    'count virus'
    chcekcount = 0
    for check in virusbody:
        if check == "o":
            chcekcount += 1
    print(chcekcount)

virus(str(input()))
