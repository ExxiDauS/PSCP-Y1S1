"""Ejudge"""
def gettime(line):
    """Get MS"""
    if line.count("time="):
        start = line.find("time=")
        end = line.find("ms")
        return int(line[start + 5:end])
    return "Nofound"
def main():
    """Ping"""
    ping = input()
    input()
    line1 = input()
    line2 = input().replace("<1", "=0")
    line3 = input().replace("<1", "=0")
    line4 = input().replace("<1", "=0")
    line5 = input().replace("<1", "=0")
    var_ip = ""
    if not ping[ping.find("ping ") + 5:][0].isdigit():
        f_ip = line1.find("[")
        b_ip = line1.find("]")
        var_ip = line1[f_ip + 1:b_ip]
    else:
        var_ip = ping[ping.find("ping ") + 5:]
    susscess = (line2 + line3 + line4 + line5).count(var_ip)
    print("Ping statistics for %s:" % (var_ip))
    print("    Packets: Sent = 4, Received = %d, Lost = %d (%s)," %
          (susscess, 4 - susscess, str((4 - susscess) * 25) + "% loss"))
    timeee = [gettime(line2), gettime(line3), gettime(line4), gettime(line5)]
    for _ in range(timeee.count("Nofound")):
        timeee.remove("Nofound")
    if len(timeee):
        print("Approximate round trip times in milli-seconds:")
        mac = max(timeee)
        meen = min(timeee)
        avg = int(sum(timeee) / len(timeee))
        print("""    Minimum = %dms, Maximum = %dms, Average = %dms""" %
              (meen, mac, avg))
main()
