"""Blackjack"""
def main():
    'Blackjack'
    total_score = 0
    card_count = 0
    card_slots = []
    card_slots_check = 0
    card_in_hand = int(input())
    while card_count < card_in_hand:
        number = input()
        card_slots.append(number)
        card_slots.sort(reverse=True)
        card_count += 1
    while card_slots_check < len(card_slots):
        if total_score >= 21:
            total_score += 0
        elif card_slots[card_slots_check] == "J" \
            or card_slots[card_slots_check] == "Q" \
            or card_slots[card_slots_check] == "K":
            total_score += 10
        elif card_slots[card_slots_check] == "A":
            if total_score < 10:

                total_score += 11
            else:
                total_score += 1
        else:
            total_score += int(card_slots[card_slots_check])
        card_slots_check += 1
    if total_score > 21:
        if bool(card_slots.count("A")) == True:
            total_score -= 10
    print(total_score)
main()
