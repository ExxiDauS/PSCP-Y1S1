"""Ejudge"""
def main():
    """Squid Game 3 - Tug-of-War"""
    teama = 0
    teamb = 0
    for _ in range(10):
        peoplea = int(input())
        teama += peoplea
    for _ in range(10):
        peopleb = int(input())
        teamb += peopleb
    if teama > teamb:
        print("B")
    elif teama < teamb:
        print("A")
    else:
        print("AB")
main()
