"""Elo"""

def elohell(rank_a, rank_b, a_or_b):
    'use equation'
    rank_rate_a = (1/(1+10**((rank_b - rank_a)/400)))
    rank_rate_b = (1/(1+10**((rank_a - rank_b)/400)))
    if rank_rate_a + rank_rate_b != 1:
        return
    if a_or_b == "A":
        print("%.2f" % rank_rate_a)
    elif a_or_b == "B":
        print("%.2f" % rank_rate_b)
    else:
        return

elohell(int(input()), int(input()), str(input()))
