"""RockPaperScissor"""

def rpscheck(result):
    'string slice to loop'
    startnum = 0
    stopnum = 2
    score_a = 0
    score_b = 0
    for _ in range(int(abs(len(result) / 2))):
        if result[startnum:stopnum] == "SP":
            score_a += 1
        elif result[startnum:stopnum] == "PR":
            score_a += 1
        elif result[startnum:stopnum] == "RS":
            score_a += 1
        elif result[startnum:stopnum] == "PS":
            score_b += 1
        elif result[startnum:stopnum] == "RP":
            score_b += 1
        elif result[startnum:stopnum] == "SR":
            score_b += 1
        else:
            score_b += 0
        startnum += 2
        stopnum += 2
    if score_a == score_b:
        print("DRAW", score_a)
    elif score_a > score_b:
        print("A win", str(score_a) + "-" + str(score_b))
    elif score_b > score_a:
        print("B win", str(score_b) + "-" + str(score_a))
rpscheck(str(input()))
