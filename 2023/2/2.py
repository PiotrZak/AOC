import re

with open('2.txt', 'r') as f:
    lines = f.read().split('\n')


colors = ['red', 'green', 'blue']
possible_limit = {'red': 12, 'green': 13, 'blue': 14}

reset_sign = ';'
game_identifier = ':'

#there pattern for group numbers is necessary
#['100'] instead ['1', '0', '0']

num_pattern = re.compile(r'(\d+)')


def check_if_exceed_limit(bag):
    for color in colors:
        if bag[color] >= possible_limit[color]:
            return False
    return True

games_ids = 0

for game in lines:
    
    game_id = num_pattern.findall(game.split(game_identifier)[0])
    game_bag = {"gameid": game_id, "red": 0, "green": 0, "blue": 0, "possible": False}

    sets_with_game = game.split(reset_sign)
    
    # ['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']
    sets = [s.split(':', 1)[-1].strip() for s in sets_with_game]

    for set_str in sets:
        set_items = set_str.split(',')
        for item in set_items:
            quantity, color = item.strip().split(' ')
            quantity = int(quantity)
            game_bag[color] += quantity
    game_bag["possible"] = check_if_exceed_limit(game_bag)
    print(game_bag)

    if game_bag["possible"]:
        games_ids += int(game_bag["gameid"][0])

# Total game IDs where all sets are possible: 78 (after all sets with colors summed)
# strange it's seems that only one game with id 78 is possible.
print(games_ids)