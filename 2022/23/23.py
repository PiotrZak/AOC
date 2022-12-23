# from collections import Counter, defaultdict
# P = complex
# import numpy as np

# data = open("23.txt", "r").readlines()

# rounds = 10
# directions = {
#     "N": (0, 1),
#     "NE": (1, 1),
#     "E": (1, 0),
#     "SE": (1, -1),
#     "S": (0, -1),
#     "SW": (-1, -1),
#     "W": (-1, 0),
#     "NW": (-1, 1),
# }

# #If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
# #If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
# #If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
# #If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.

# def adjacent(x, y):
#     return [(x + dx, y + dy) for dx, dy in directions.values() if (x + dx, y + dy) in board]


# def adjacent_occupied(x, y):
#     print(x, y)
#     return [(((x+dx, y+dy), board[(x + dx, y + dy)])) for dx, dy in directions.values() if (x + dx, y + dy) in board]


# def draw_board (board, point):

#     max_x = max([x for x, y in board.keys()])
#     max_y = max([y for x, y in board.keys()])

#     for y in range(max_y):
#         for x in range(max_x):
#             if (x, y) == point:
#                 print("X", end="")
#             elif board[(x, y)] == True:
#                 print("#", end="")
#             else:
#                 print(".", end="")
#         print()

# def gen_board(data):
#   board = {}
#   for y, line in enumerate(data):
#       for x, char in enumerate(line):
#           if char == "#":
#               board[(x, y)] = True
#           else:
#               board[(x, y)] = False
#   return board

# def filter_elves(board):
#   elves = []
#   for elv in board:
#       if board[elv] == True:
#           elves.append(elv)
#   return elves

# board = gen_board(data)
# elves = filter_elves(board)

# neighbours = adjacent(0, 0)
# is_occupied = adjacent_occupied(1, 1)
# print(is_occupied)
# draw_board(board, (1, 1))

# while rounds:

#   new_board = board.copy()

#   for elv in new_board:
#       if new_board[elv] == True:
#           continue


#   rounds -= 1


from collections import defaultdict


demo = (
"..............\n" 
".............. \n"
".......#......\n"
".....###.#....\n"
"...#...#.#....\n"
"....#...##....\n"
"...#.###......\n"
"...##.#.##....\n"
"....#..#......\n"
"..............\n" 
".............. \n"
"..............\n" 
)

def get_grid():
    #T = open("23-demo.txt").read().split('\n')
    T = demo.split('\n')
    print(T)
    return {x + 1j * y for y, l in enumerate(T) for x, c in enumerate(l) if c == '#'}

neighbors = lambda p: [p - 1, p + 1, p - 1j, p + 1j, p + 1 + 1j, p + 1 - 1j, p - 1 + 1j, p - 1 - 1j]
def elf_move(grid, p, round_no):
    if all(not p1 in grid for p1 in neighbors(p)):
        return p

## #If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
# #If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
# #If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
# #If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.
    moves_ops = [([p - 1j, p + 1 - 1j, p - 1 - 1j], p - 1j),
                 ([p + 1j, p + 1 + 1j, p - 1 + 1j], p + 1j),
                 ([p - 1 + 1j, p - 1 - 1j, p - 1], p - 1),
                 ([p + 1 + 1j, p + 1 - 1j, p + 1], p + 1)]
    for i in range(round_no, round_no + 4):
        if all(p1 not in grid for p1 in moves_ops[i % len(moves_ops)][0]):
            return moves_ops[i % len(moves_ops)][1]
    return p

def do_round(grid, round_no):
    did_move, moves, new_grid = False, defaultdict(list), set()
    for elf in grid:
        new_p = elf_move(grid, elf, round_no)
        if new_p != elf:
            did_move = True
        moves[new_p].append(elf)
    for k, v in moves.items():
        if len(v) == 1:
            new_grid.add(k)
        else:
            new_grid.update(v)
    return new_grid, did_move

def part1():
    grid = get_grid()
    for round_no in range(10):
        grid, _ = do_round(grid, round_no)
    ys = sorted([i.imag for i in grid])
    xs = sorted([i.real for i in grid])
    print((xs[-1] - xs[0] + 1) * (1 + ys[-1] - ys[0]) - len(grid))

def part2():
    did_move, grid, round_no = True, get_grid(), 0
    while did_move:
        grid, did_move = do_round(grid, round_no)
        round_no += 1
    print(round_no)

part1()
part2()
