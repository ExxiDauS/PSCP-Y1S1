"""FoodGrade I"""


def food(chicken, number01):
    "food"
    if chicken > 0:
        weight = float(input())
        if weight >= 50 and weight <= 70:
            number01 += 1
    else:
        print(number01)
        return
    food(chicken - 1, number01)


def counntjingjing():
    "num"
    countnaja = 0
    food(24, countnaja)


counntjingjing()
