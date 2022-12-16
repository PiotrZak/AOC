import re
from collections import defaultdict

stacks = defaultdict(list)

for line in open('5.txt'):
    if '[' in line:
        for i in range(1, len(line) - 1, 4):
            if line[i] != ' ':
                stacks[(i - 1) // 4].append(line[i])

    elif line.startswith('move'):
        # finding every ints from 'move 1 from 8 to 4' and converting them to int
        numberOfLetters, start, end = map(int, re.findall(r'\d+', line))
        # add the letters from the end stack
        # for p2 - remove [::-1] - it reverses the list
        stacks[end - 1] = stacks[start - 1][:numberOfLetters][::-1] + stacks[end - 1]
        # remove the letters to the start stack
        stacks[start - 1] = stacks[start - 1][numberOfLetters:]

print(''.join(stacks[i][0] for i in range(len(stacks))))


#a[::-1]    # all items in the array, reversed
#a[1::-1]   # the first two items, reversed
#a[:-3:-1]  # the last two items, reversed
#a[-3::-1]  # everything except the last two items, reversed

#mylist[X:Y]
#X is the index of the first element you want.
#Y is the index of the first element you don't want.