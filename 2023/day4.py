

import re

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

def main(data):
    score = 0
    for line in data.split("\n"):
        game = line.split(": ")[1]
        winning_numbers = get_winning(game)
        player_numbers = get_player(game)
        win_count = wining_count(set(winning_numbers), set(player_numbers))
        score += calc_winning_points(win_count)

    return score

if __name__ == "__main__":
    import os
    HERE = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(HERE, "../data/2023/4.txt"), "r") as data:
        print(main(data.read()))