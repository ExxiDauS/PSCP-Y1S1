"""[Midterm 2021 + Recommend] Century"""

def year(amount):
    'A.D B.E'

    if amount == 0:
        print("ERROR")
    for _ in range(amount):
        century = ""
        start = str(input())
        if start.find('A.D.') != -1:
            start = start.replace("A.D.", "")
            start = int(start.strip())
            if start <= 0:
                century += "ERROR"
            elif start % 100 == 0:
                century += str(start // 100)
            else:
                century += str((start // 100) + 1)
            print(century)
        else:
            start = start.replace("B.E.", "")
            start = int(start.strip()) - 543
            if start <= 0:
                century += "ERROR"
            elif start % 100 == 0:
                century += str(start // 100)
            else:
                century += str((start // 100) + 1)
            print(century)
year(int(input()))
