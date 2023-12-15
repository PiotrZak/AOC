import re

with open('2.txt', 'r') as f:
    lines = f.read().split('\n')

colors = ['red', 'green', 'blue']
possible_limit = {'red': 12, 'green': 13, 'blue': 14}

reset_sign = ';'
game_identifier = ':'
num_pattern = re.compile(r'(\d+)')

def check_if_exceed_limit(bag):
    return all(bag.get(color, 0) <= possible_limit[color] for color in colors)

games_ids = 0

for game in lines:
    game_id = int(num_pattern.search(game.split(game_identifier)[0]).group(1))

    sets_with_game = game.split(reset_sign)

    # ['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']
    sets = [s.split(':', 1)[-1].strip() for s in sets_with_game]


    game_possible = all(
        check_if_exceed_limit({
            color: int(quantity)
            for quantity, color in (item.strip().split(' ') for item in set_str.split(','))
        })
        for set_str in sets
    )

    if game_possible:
        games_ids += game_id

print("Total game IDs where all sets are possible:", games_ids)