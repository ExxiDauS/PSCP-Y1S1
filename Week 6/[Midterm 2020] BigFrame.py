"""BigFrame"""

def bigframe():
    'using len'
    msg01 = str(input()).strip()
    msg02 = str(input()).strip()
    msg03 = str(input()).strip()
    msg04 = str(input()).strip()
    msg05 = str(input()).strip()
    space = max(len(msg01), len(msg02), len(msg03), len(msg04), len(msg05))
    print("*" * (space + 4))
    print("*", msg01 + " " * abs(len(msg01) - space), "*")
    print("*", msg02 + " " * abs(len(msg02) - space), "*")
    print("*", msg03 + " " * abs(len(msg03) - space), "*")
    print("*", msg04 + " " * abs(len(msg04) - space), "*")
    print("*", msg05 + " " * abs(len(msg05) - space), "*")
    print("*" * (space + 4))
bigframe()
