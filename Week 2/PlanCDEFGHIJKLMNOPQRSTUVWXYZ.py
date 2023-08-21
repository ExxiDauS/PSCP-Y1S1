"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main():
    """mix max without using it"""
    tmp = input().lower()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if tmp == "descend":
        big(num1, num2, num3)
    elif tmp == "ascend":
        small(num1, num2, num3)
def big(num1, num2, num3):
    """bigger"""
    if num1 >= num2 and num1 >= num3:
        if num2 > num3:
            print("%.2f, %.2f, %.2f" %(num1, num2, num3))
        else:
            print("%.2f, %.2f, %.2f" %(num1, num3, num2))
    elif num2 >= num1 and num2 >= num3:
        if num1 > num3:
            print("%.2f, %.2f, %.2f" %(num2, num1, num3))
        else:
            print("%.2f, %.2f, %.2f" %(num2, num3, num1))
    elif num3 >= num1 and num3 >= num2:
        if num1 > num2:
            print("%.2f, %.2f, %.2f" %(num3, num1, num2))
        else:
            print("%.2f, %.2f, %.2f" %(num3, num2, num1))
def small(num1, num2, num3):
    """smaller"""
    if num1 <= num2 and num1 <= num3:
        if num2 < num3:
            print("%.2f, %.2f, %.2f" %(num1, num2, num3))
        else:
            print("%.2f, %.2f, %.2f" %(num1, num3, num2))
    elif num2 <= num1 and num2 <= num3:
        if num1 < num3:
            print("%.2f, %.2f, %.2f" %(num2, num1, num3))
        else:
            print("%.2f, %.2f, %.2f" %(num2, num3, num1))
    elif num3 <= num1 and num3 <= num2:
        if num1 < num2:
            print("%.2f, %.2f, %.2f" %(num3, num1, num2))
        else:
            print("%.2f, %.2f, %.2f" %(num3, num2, num1))
main()
