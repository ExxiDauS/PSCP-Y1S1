"""Ejudge"""
def main():
    """Shorten"""
    tmp = ""
    start = None
    prev = None
    while True:
        num = int(input())
        if num == -1:
            break
        if start == None:
            start = num
            prev = num
            continue
        else:
            if prev != num-1:
                if start == prev:
                    tmp += "%d, " % start
                else:
                    tmp += "%d-%d, " % (start, prev)
                start = num
                prev = num
            else:
                prev = num
    if start != None:
        if start == prev:
            tmp += "%d, " % start
        else:
            tmp += "%d-%d" % (start, prev)
    print(tmp.strip(", "))
main()
