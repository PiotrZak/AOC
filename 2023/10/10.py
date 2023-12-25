# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.

# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

# .....
# .F-7.
# .|.|.
# .L-J.
# .....

# Starting point connects to the pipes
# Imaginary numbers for reflecting the coords (x, y) of current step to the path from start
# https://en.wikipedia.org/wiki/Imaginary_number


data =[['.']+[y for y in x]+['.'] for x in open('10.txt').read().split('\n')]
data = [['.'] * len(data[0])] + data + [['.'] * len(data[0])]


maze = {}
direcs = {
    'F': [0 + 1j, 1 + 0j],
    '7' : [-1 + 0j, 0 + 1j ] ,
    'J' : [0 - 1j, -1 + 0j], 
    'L': [1 + 0j, 0 - 1j], 
    '-' : [1 + 0j, -1 + 0j], 
    '|' : [0 + 1j, 0 - 1j], 
    '.' : [] 
    }
for h in range(len(data)):
    for w in range(len(data[0])):
        if data[h][w] == 'S':
            start = complex(w,h)
        maze[complex(w,h)] = data[h][w]


def get_neighs(z):    
    if maze[z] != 'S':
        return([z + w for w in direcs[maze[z]]])
    else: #starting point
        neighbors = [z + (1 + 0j), z + (-1 + 0j), z + (1 + 1j), z + (-1 + 1j), z + (1 - 1j), z + (-1 - 1j), z + (0 + 1j), z + (0 - 1j)]
        return([n for n in neighbors if z in [n + w for w in direcs[maze[n]]]])

cur = get_neighs(start)[0]
path = set([cur])

while True:
    new = [x for x in get_neighs(cur) if x not in path]
    if len(new) > 0:
        path.add(new[0])
        cur = new[0]
    else:
        break

print(path)
    
print(len(path)//2 )


