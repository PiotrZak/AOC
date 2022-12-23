
from collections import defaultdict, deque
import re

board = {}
row_ends = {}
col_ends = {}
cur = None



voids = []

map, ins = open('22.txt').read().split('\n\n')

rotations = {'L': -1, 'R': 1}
diagonals = {(1, 1): '\\', (1, -1): '/', (-1, 1): '/', (-1, -1): '\\'}

#print(map)

def gen_map():
    m = defaultdict(lambda: 0)
    for numberOfLine, l in enumerate(map.strip().split('\n')):
        for x, c in enumerate(l):
            if c == ' ':
                voids.append(((x, numberOfLine)))
            m[x, numberOfLine] = c == '.'
    return m


map = gen_map()


# rotation

start_pos = (0, 0)
positions = []
facing = 0
facing = deque(['North', 'East', 'South', 'West'])
direction = 4

path = tuple(re.findall("[0-9]+|[LR]", ins))
path_pairs = zip(path[::2], path[1::2])

def move(map, facing, distance, start_pos):
    #move to the facing direction

    for i in range(int(distance)):
        
        if 'next_pos' in locals():
            pos = next_pos 
        else:
            pos = start_pos

        if facing[0] == 'North':
            next_pos = (pos[0], pos[1] - 1)
        elif facing[0] == 'East':
            next_pos = (pos[0] + 1, pos[1])
        elif facing[0] == 'South':
            next_pos = (pos[0], pos[1] + 1)
        elif facing[0] == 'West':
            next_pos = (pos[0] - 1, pos[1])

    return next_pos

for distance, rotation in path_pairs:

    if rotation == 'R':
        facing.rotate(-1)
    if rotation == 'L':
        facing.rotate(1)

    current_trace = move(map, facing, distance, (0, 0))

    print(current_trace)



import sys
lines = [x.rstrip() for x in open("22.txt").readlines()]
board = lines[:-2]
ops = lines[-1]

wrap = {}
def edge(face1, dir1, exit, face2, dir2, enter, rot):
  for k in range(50):
    p1 = (face1[0] + dir1[0] * k, face1[1] + dir1[1] * k)
    p2 = (face2[0] + dir2[0] * k, face2[1] + dir2[1] * k)
    wrap[(p1[0] + exit[0], p1[1] + exit[1])] = (p2, rot)
    wrap[(p2[0] + enter[0], p2[1] + enter[1])] = (p1, -rot)

# Front:
edge((0, 50), (1, 0), (0, -1), (149, 0), (-1, 0), (0, -1), 2) # Left
edge((0, 50), (0, 1), (-1, 0), (150, 0), (1, 0), (0, -1), 1) # Top

# Right:
edge((49, 100), (0, 1), (1, 0), (50, 99), (1, 0), (0, 1), 1) # Under
edge((0, 100), (0, 1), (-1, 0), (199, 0), (0, 1), (1, 0), 0) # Top
edge((0, 149), (1, 0), (0, 1), (149, 99), (-1, 0), (0, 1), 2) # Back

# Under:
edge((50, 50), (1, 0), (0, -1), (100, 0), (0, 1), (-1, 0), 3) # Left

# Back:
edge((149, 50), (0, 1), (1, 0), (150, 49), (1, 0), (0, 1), 1) # Top

dir = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
p,facing = (0, board[0].index('.')),0
i = step = 0
trace = [ list(r) for r in board ]
while i < len(ops):
  step += 1
  if ops[i] == 'L':
    facing = (facing-1) % 4
    i += 1
  elif ops[i] == 'R':
    facing = (facing+1) % 4
    i += 1
  else:
    steps = ''
    while i < len(ops) and ops[i].isnumeric():
      steps += ops[i]
      i += 1
    for k in range(int(steps)):
      r1,c1 = p[0] + dir[facing][0], p[1] + dir[facing][1]
      f0 = facing

      if (r1,c1) in wrap:
        (r1,c1),ff = wrap[(r1,c1)]
        facing = (facing + ff) % 4

      if board[r1][c1] == '#':
        facing = f0
        break
      trace[p[0]][p[1]] = '>v<^'[f0]
      p = (r1,c1)
  if len(sys.argv) > 1 and step == int(sys.argv[1]): break
trace[p[0]][p[1]] = 'o'
for b in trace:
  print(''.join(b))
end = (p[0]+1, p[1]+1)
print(f'end pos = {end}')
print(f'answer = {end[0]*1000 + end[1]*4 + facing}')
    

# data = open("22.txt", "r").read().split("\n\n")

# r = 0
# for inp in data[0].split("\n"):
#     r += 1
#     for c, v in enumerate(inp, 1):
#         if v != " ":
#             board[r, c] = True if v == "." else False
#             if board.get((r - 1, c)) == None:
#                 col_ends[c] = (r, None)
#             else:
#                 col_ends[c] = (col_ends[c][0], r)
#             if not cur and r == 1:
#                 cur = (1, c)
#             row_ends[r] = (row_ends.get(r, (c,))[0], c)

# path = tuple(re.findall("[0-9]+|[LR]", data[1]))

# for cmd in path:
#     if cmd.isdigit():
#         steps = int(cmd)
#         dp, di = not facing in (1, 3), (1, -1)[facing in (2, 3)]
#         for _ in range(steps):
#             new = cur[dp] + di
#             ends = (col_ends, row_ends)[dp][cur[~dp]]
#             if new < ends[0] or new > ends[1]:
#                 new = ends[0] if di == 1 else ends[1]
#             if not board[(new_pos := (cur[~dp], new) if dp else (new, cur[~dp]))]:
#                 break
#             cur = new_pos
#     elif cmd == "R":
#         facing = (1, 2, 3, 0)[facing]
#     else:
#         facing = (3, 0, 1, 2)[facing]


# instructions = []
# map = []

# for line in open("22.txt").readlines():
    
#     if (line.startswith('17R')):
#         instructions.append(line.strip('\n'))
#     else:
#         map.append(line.strip('\n'))


# def generate_map(map):
#     map = [list(x) for x in map]
#     for y in range(len(map)):
#         for x in range(len(map[y])):
#             if map[y][x] == '#':
#                 map[y][x] = 1
#             else:
#                 map[y][x] = 0
#     return map



# map = generate_map(map)




# right = {0, '>'}
# bottom = {1, 'v'}
# top = {3, '^'}
# left = {2, '<'}

# instructions = slice_instructions(instructions[0])
# print(instructions)


# 10 R 5 -> means forward 10 - then turn 90 degrees - then forward 5


