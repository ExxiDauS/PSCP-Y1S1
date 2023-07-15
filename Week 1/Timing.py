"Timing"
def main():
    'var test'
    second = int(input())
    minutes = second//60
    second = second%60
    hours = minutes//60
    minutes = minutes%60
    days = hours//24
    hours = hours%24
    print(days, hours, minutes, second)
main()
