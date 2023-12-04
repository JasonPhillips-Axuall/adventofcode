

import re

def get_card_number(line):
    return int(line.split(":")[0].split()[1])

def get_winning(line):
    return set([int(s.strip()) for s in re.findall(r'\d+', line.split(' | ')[1])])

def get_player(line):
    return set([int(s.strip()) for s in re.findall(r'\d+', line.split(' | ')[0])])

def wining_count(player_set, winning_set):
    return len(player_set.intersection(winning_set))

def calc_winning_points(winning_number):
    if(winning_number == 0):
        return 0

    return 2 ** (winning_number -1)

def add_card(cache):
    retval = []
    queue = [k for k in cache.keys()]
    while len(queue) > 0:
        card_number = queue.pop(0)
        retval.append(card_number)
        if card_number in cache:
            multiplier = retval.count(card_number)
            
            if(multiplier == 0):
                multiplier = 1

            add_to_cache = []
            for i in range(0, multiplier):
                add_to_cache += cache[card_number]

            cache[card_number] = add_to_cache
            tmp = retval + add_to_cache
            retval = tmp
    
    return len(retval)


def main(data):

    cache = {}

    score = 0

    # calc points
    for line in data.split("\n"):
        game = line.split(": ")[1]
        winning_numbers = get_winning(game)
        player_numbers = get_player(game)
        matches = wining_count(set(winning_numbers), set(player_numbers))
        
        card_number = get_card_number(line)
        cache[card_number] = [i+card_number+1 for i in range(0, matches)]
        
        points = calc_winning_points(matches)
            
        score += points

    card_count = add_card(cache)

    # calc cards

    return score, card_count

if __name__ == "__main__":
    import os
    HERE = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(HERE, "../data/2023/4.txt"), "r") as data:
        print(main(data.read()))