"""SurprisingVote"""


def vote(total_score, high_score):
    "vote"
    second_vote = min(total_score - high_score, high_score)
    third_vote = total_score - (high_score + second_vote)
    print("Surprising" if (high_score - third_vote) > 2 else "Not surprising")


vote(float(input()), float(input()))
