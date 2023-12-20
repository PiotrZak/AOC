
#Author: https://www.reddit.com/user/Sbgodin/

INPUT = "7test.txt"

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

hands = tuple((l[0], int(l[1])) for l in map(lambda s:s.split(), open(INPUT).read().splitlines()))

print(hands)


# l.just - adding the char after string
# first argument is the length of the string
# second argument is the char to add

#zfill - adding the char before

key = lambda hand: int(
    ''.join(str(c) 
        for c in sorted((hand[0].count(x) for x in set(hand[0])), reverse=True))
    .ljust(5, '0') + ""
    .join(str(cards.index(x) + 1)
    .zfill(2) for x in hand[0]))
    

sortedHands = sorted(hands,key=key)
total = sum(map(lambda x: (x[0] + 1) * x[1][1], enumerate(sortedHands)))

print("TOTAL", total)
