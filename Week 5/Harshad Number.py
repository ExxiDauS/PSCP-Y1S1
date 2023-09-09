"""Harshad Number"""

def harshad():
    'nested loop'
    summary = 0
    for _ in range(10):
        number = int(input())
        for char in str(abs(number)):
            summary += int(char)
        if number == 0:
            print("No")
        elif number % summary != 0:
            print("No")
        else:
            print("Yes")
        summary = 0

harshad()
