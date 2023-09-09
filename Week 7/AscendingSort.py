"""AscendingSort"""

def ascend():
    'ascend'
    txt = []
    for num in range(0, 5):
        txt.append(int(input()))
    txt.sort()
    for num in txt:
        print(num)
ascend()
