"""Kayak"""
def main():
    'kayak'
    numbersofpeople = int(input()) * 2
    numbers = [int(num) for num in input().split(" ", numbersofpeople-1)]
    print(numbers)
    for i in range(0,2):
        numbers.remove(max(numbers))
    numbers.sort()
    print()
main()
