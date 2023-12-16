import re

with open('4.txt', 'r') as f:
    cards = f.read().split('\n')

points = 0

for card in cards:
    win, lottery = card.split('|')
    card, win = win.split(":")

    win_nums = set(map(int, re.findall(r'\d+', win)))
    lottery_nums = set(map(int, re.findall(r'\d+', lottery)))

    lucky_common = win_nums.intersection(lottery_nums)

    if lucky_common:
        # This is a common approach in scoring systems
        # where more significant matches are rewarded more generously.
        points += 2 ** (len(lucky_common) - 1)

print(points)
## ** - in python 3 ** 3 = 27, 9 ** 9 = 81
## 2 ** 0 = 1


    # results of lucky_common:

    # {'17', '83', '86', '48'}
    # {'61', '32'}
    # {'21', '1'}
    # {'84'}
    # set()
    # set()

    # Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
    # Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
    # Card 4 has one winning number (84), so it is worth 1 point.
    # Card 5 has no winning numbers, so it is worth no points.
    # Card 6 has no winning numbers, so it is worth no points.