with open('2.txt', 'r') as f:
    g = f.read().split('\n\n')

#p1
pairs = []
points = 0
draw = 3
win = 6
lose = 0

for i in range(len(g)):
    g[i] = g[i].replace('\n', ' ')
    g[i] = g[i].split(' ')
    pairs.append(g[i])

pairs = ([(pairs[0][i],pairs[0][i+1]) for i in range(0,len(pairs[0]),2)])
for i in range(len(pairs)):

    if (pairs[i][0] == 'A' and pairs[i][1] =='X'):
        points += draw + 1

    elif (pairs[i][0] == 'A' and pairs[i][1] =='Y'):
        points += win + 2

    elif (pairs[i][0] == 'A' and pairs[i][1] =='Z'):
        points += lose + 3

    elif (pairs[i][0] == 'B' and pairs[i][1] =='X'):
        points += lose + 1

    elif (pairs[i][0] == 'B' and pairs[i][1] =='Y'):
        points += draw + 2

    elif (pairs[i][0] == 'B' and pairs[i][1] =='Z'):
        points += win +3

    elif (pairs[i][0] == 'C' and pairs[i][1] =='X'):
        points += win + 1

    elif (pairs[i][0] == 'C' and pairs[i][1] =='Y'):
        points += lose + 2

    elif (pairs[i][0] == 'C' and pairs[i][1] =='Z'):
        points += draw + 3

print(points)
#p2 - author - Alex Telon 

with open('2.txt', 'r') as f:
    lines = f.read().splitlines()

convert = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}
def lose_to(a):
    i = ['paper', 'rock', 'scissors'].index(a)
    return ['paper', 'rock', 'scissors', 'paper'][i+1]

def win_to(a):
    i = ['paper', 'rock', 'scissors'].index(a)
    return ['paper', 'rock', 'scissors'][i-1]

def draw_to(a):
    return a

def me_won(elf, me):
    return me == win_to(elf)

score = 0
for line in lines:
    elf, me = line.split()
    elf = convert[elf]
    me  = convert[me]
    if    me == 'lose': me = lose_to(elf)
    elif  me == 'draw': me = draw_to(elf)
    else:               me = win_to(elf)
    score += [' ', 'rock', 'paper','scissors'].index(me)
    if me_won(elf, me):
        score += 6
    elif me == elf:
        score += 3

print(score)