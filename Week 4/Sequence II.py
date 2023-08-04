"""Sequence II"""


def seq2(number):
    "count"
    plus = 1
    summary = 0
    for _ in range(0, number):
        summary += plus
        print(summary, end=" ")
        plus += 2


seq2(int(input()))
