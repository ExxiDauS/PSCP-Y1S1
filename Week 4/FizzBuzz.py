"""FizzBuzz"""


def test(number):
    """fizz and buzz"""
    if number <= 0:
        return
    for countnumber in range(1, number + 1):
        if countnumber % 3 == 0 and countnumber % 5 == 0:
            print("FizzBuzz")
        elif countnumber % 3 == 0:
            print("Fizz")
        elif countnumber % 5 == 0:
            print("Buzz")
        else:
            print(countnumber)


test(int(input()))
