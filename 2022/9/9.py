data = open("9.txt").read().strip().split("\n")

rope = [0 + 0j] * 2  # * 10 for part 2

# In python, you can put ‘j’ or ‘J’ after a number to make it imaginary, so you can write complex literals easily:
# j - represent the y axis (poziom)

moves = {"L": -1j, "R": 1j, "U": 1, "D": -1}
hist = set(rope)

for line in data:
    direction, fieldToMove = line[0], int(line[2:])

    #  iteration of every field in one of 4 directions
    for _ in range(fieldToMove):

        print(rope[0])
        rope[0] += moves[direction]
        for i in range(1, 2):
            if abs((d := rope[i - 1] - rope[i])) >= 2:
                move = int(d.real / 2) + 1j * int(d.imag / 2)
                rope[i] = rope[i - 1] - move
        hist.add(rope[-1])

print(len(hist));

# # another solution - znipper-  Reddit author
# import sys 

# def move(f):
#     x = y = 0 
#     for line in f:
#         direction, distance = line.split()
#         for _ in range(int(distance)):
#             x += (direction == 'R') - (direction == 'L')
#             y += (direction == 'U') - (direction == 'D')
#             yield x, y

# def follow(head):
#     x = y = 0 
#     for hx, hy in head:
#         if abs(hx - x) > 1 or abs(hy - y) > 1:
#             y += (hy > y) - (hy < y)
#             x += (hx > x) - (hx < x)
#         yield x, y

# tenth = second = list(follow(move(sys.stdin)))
# for _ in range(8):
#     tenth = follow(tenth)
# print(len(set(second)))
# print(len(set(tenth)))


#another solution:

# from math import dist

# def update_heads(last_heads, step):
#     d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

#     heads_x = last_heads[0]
#     heads_y = last_heads[1]
#     heads_x += d[step[0]][0]
#     heads_y += d[step[0]][1]



#     return ((heads_x, heads_y))

# def update_tails(last_heads, last_tails):
#     Hx = last_heads[0]
#     Hy = last_heads[1]
#     Tx = last_tails[0]
#     Ty = last_tails[1]
#     if abs(Ty - Hy) > 1 and Tx == Hx:
#         Ty += [-1, 1][Ty < Hy]
#     elif abs(Tx - Hx) > 1 and Ty == Hy:
#         Tx += [-1, 1][Tx < Hx]
#     elif dist((Hx,Hy),(Tx,Ty)) > 2:
#         Tx += [-1, 1][Tx < Hx]
#         Ty += [-1, 1][Ty < Hy]
#     A = (Tx, Ty)
#     print(A)
#     return A



# with open('9.txt') as file:
#     lines = file.readlines()

#     lines = [[x,int(y)] for [x,y] in [_.rstrip().split(" ") for _ in lines]]
#     last_heads = [0, 0]
#     last_tails = (0,0)
#     visited = [last_tails]

#     for item in lines:
#         for i in range(item[1]):
#             last_heads = update_heads(last_heads, item)
#             last_tails = update_tails(last_heads, last_tails)
#             visited.append(last_tails)


#     print(len(set(visited)))


    # solution by kresimir-lukin


# import sys

# def move(segments, direction):
#     offsets = {'L': (-1, 0), 'U': (0, 1), 'R': (1, 0), 'D': (0, -1)}
#     dx, dy = offsets[direction]
#     segments[0][0] += dx
#     segments[0][1] += dy
#     for segment_index in range(1, len(segments)):
#         previous = segments[segment_index-1]
#         current = segments[segment_index]
#         if max(abs(previous[0] - current[0]), abs(previous[1] - current[1])) > 1:
#             if previous[0] != current[0]:
#                 current[0] += 1 if previous[0] > current[0] else -1
#             if previous[1] != current[1]:
#                 current[1] += 1 if previous[1] > current[1] else -1

# def simulate(moves, segment_count):
#     segments = [[0, 0] for _ in range(segment_count)]
#     tail_positions = set([tuple(segments[-1])])
#     for direction, steps in moves:
#         for _ in range(steps):
#             move(segments, direction)
#             tail_positions.add(tuple(segments[-1]))
#     return len(tail_positions)

# moves = sys.stdin.read().splitlines()
# moves = [(move.split()[0], int(move.split()[1])) for move in moves]

# print(f'Part 1: {simulate(moves, 2)}, Part 2: {simulate(moves, 10)}')



