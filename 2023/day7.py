
from itertools import groupby

suit = ['J', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', '', 'Q', 'K', 'A']

def group_hand(hand):
    joker_count = hand.count('J')
    
    if joker_count > 0:
        hand = [*''.join(hand).replace('J', '')]

    sorted_hand = groupby(sorted(hand, key=lambda x: hand_value(x[0])))
    groups = [(c,len(list(cgen))) for c,cgen in sorted_hand]
    
    if len(groups) == 0:
        return [('1',5)]

    if joker_count > 0:
        group = groups.pop(0)
        group = (group[0], group[1] + joker_count)
        groups.append(group)

    return groups

def is_five_of_a_kind(hand):
    groups = group_hand(hand)
    return any([v == 5 for _,v in groups])

def is_four_of_a_kind(hand):
    groups = group_hand(hand)
    return any([v >= 4 for _,v in groups])

def is_full_house(hand):
    groups = group_hand(hand)
    is_5 = any([v == 5 for _,v in groups])
    has_3 = any([v == 3 for _,v in groups])
    has_2 = any([v == 2 for _,v in groups])
    return (has_3 and has_2) or is_5

def is_3_of_a_kind(hand):
    groups = group_hand(hand)
    is_5 = any([v == 5 for _,v in groups])
    has_3 = any([v == 3 for _,v in groups])
    has_2 = any([v == 2 for _,v in groups])
    return (has_3 and not has_2) or is_5

def is_two_pair(hand):
    groups = group_hand(hand)
    is_5 = any([v == 5 for _,v in groups])
    has_3 = any([v == 3 for _,v in groups])
    count = 0
    for _,v in groups:
        if v == 2:
            count += 1

    return  (count == 2 and not has_3) or is_5

def is_2_of_a_kind(hand):
    groups = group_hand(hand)
    is_5 = any([v == 5 for _,v in groups])
    has_3 = any([v == 3 for _,v in groups])
    count = 0
    for _,v in groups:
        if v == 2:
            count += 1

    return  (count >= 1 and not has_3) or is_5

def trade(c):
    return str(suit.index(c)).rjust(2, '0')

def hand_value(hand):
    retval =  ''.join([str(trade(c)) for c in hand])
    return retval

def calc_hand(hand):
    flags = [is_five_of_a_kind(hand) * 1,
            is_four_of_a_kind(hand) * 1,
            is_full_house(hand) * 1,
            is_3_of_a_kind(hand) * 1,
            is_two_pair(hand) * 1,
            is_2_of_a_kind(hand) * 1,
            True * 1]
    return  ''.join(map(str, (flags)))

def main(data):
    hands = []
    for h in data.split('\n'):
        h = h.split(' ')
        poker_hand_flags = eval('0b' + calc_hand(list(h[0])))
        poker_hand_value = int(hand_value(h[0]))
        poker_hand_str = h[0]
        hands.append([int(h[1]), poker_hand_flags, poker_hand_value, poker_hand_str])

    retval = 0

    sorted_hands = sorted(hands, key=lambda x: (x[1], x[2]))
    for i, h in enumerate(sorted_hands):
        retval += (h[0] * (i+1))

    return retval

if __name__ == '__main__':
    import os
    HERE = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(HERE, "../data/2023/7.txt"), "r") as data:
        print(main(data.read()))

#   249516770
    # 249491963