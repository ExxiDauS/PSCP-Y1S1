"""SecondConverter"""

def main():
    """SecondConverter"""
    time = int(input())
    second = int(input())
    minute = int(input())
    hour = int(input())
    secondtrue = time % second
    minutetrue = time // second
    hourtrue = minutetrue // minute
    minutetrue = minutetrue % minute
    hourtrue = hourtrue % hour
    if hourtrue > hour:
        hourtrue = hourtrue % hour
    print("%d:%d:%d" %(hourtrue, minutetrue, secondtrue))
main()
