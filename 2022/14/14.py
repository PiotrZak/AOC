# # - gif by Andreas Löfgren
# #https://anlo.net/aoc_2022_14.gif

#https://topaz.github.io/paste/#XQAAAQBeBQAAAAAAAAA0m0pnuFI8c/fBNAqG6qhqad37PBl4Yloau1xsavGC4hbcL/D/erlNa4UQcebeGcmTeZg3cWqr4yvfU2nayPec+X5QOeoSTazX0Zc1HNnYFmmgX8Fko4Porsp1RDVxb6/cgBOYX6HeKQNz++Snc3mZZZVgQ/EKDgLXYn8eIIJBw4p+end1BXceyDRaw5/Vr81ZjeEeDA5WXSJckPYg2p8OxqRaLAiZaQhWuigR1zP3gEolOw9TKNhtyZKCBzDuEwEq6gZ1thq2mGg79sXgEsXS3XH+khXCElLZnOiji3b0xndIikflgbgb6Czy9qrj66wPkkL0GV1Y/ZWj4NxbSj7hAbIu6RDaoLtVKa0SrHJhJh3FOwg7kQALFZXeR/GZq80dwQp0pBx+N/DQ2+Qux2HSvLhzSEutXawFDSob4p6urgCoduA7XiyFWXHEB3nl+PMReTrI+3VgizFCh7+BgKUmW2+2Q604TLLCp+3eBpl3qNYXQCxXzex5VXer5MxBjaIS+7+aNk2WzU3zQAaHDXvI4HtnDvZj7PjKMwUdz4I/fUFzhQlR6nYeLPEnn7vEkR4EzYosIQBXRAarG+b40AlhZQFA+ESo3NxmQPulby3hwbPSIv76oWARi3UdQOtTikUs/DrdjJKLRPfRaIWcVRSInHtiQQfKqn16tpRg/biWRSXHpx96S8WQY3/9Ef4y

import sys

def parse_cave():
    cave = {}

    for line in open('14.txt').readlines():
        coords = line.split(" -> ")
        for f, t in zip(coords[0::], coords[1::]):
            (fx, fy) = (int(n) for n in f.split(","))
            (tx, ty) = (int(n) for n in t.split(","))

            for x in range(min(fx, tx), max(fx, tx) + 1):
                cave[x, fy] = "#"

            for y in range(min(fy, ty), max(fy, ty) + 1):
                cave[fx, y] = "#"
                
    return cave


def bottom(cave):
    return max(y for (_, y), val in cave.items() if val == '#')

def drop_sand(cave):
    x = 500
    
    for y in range(bottom(cave)):
        if (x, y + 1) not in cave:
            pass
        elif (x - 1, y + 1) not in cave:
            x -= 1
        elif (x + 1, y + 1) not in cave:
            x += 1 
        else:
            cave[(x, y)] = "o"
            return (x, y) != (500, 0)
    
    return False



def add_floor(cave):
    bottom_y = bottom(cave)
    for x in range(-1000, 1000):
        cave[x, bottom_y + 2] = "#"


def printboard(cave):
    mx = max(x for x,_ in cave.keys() )
    my = max(y for _,y in cave.keys() )
    for y in range(0, my+1): 
        for x in range(350, mx+1):
            if(x == 500 and y == 0):
                print("+", end='')
            if (x, y) in cave:
                print(cave[x, y], end='')
            else:
                print('.', end='')
        print('.\n')

cave = parse_cave()

def do_simulation(bottom_is_abyss):
    cave = parse_cave()
    i = 0

    if not bottom_is_abyss:
        add_floor(cave)

    while drop_sand(cave):
        i += 1
        if i >= 901:
            printboard(cave)
        pass

    return cave

print("1:", sum(1 for v in do_simulation(True).values() if v == 'o'))
#print("2:", sum(1 for v in do_simulation(False).values() if v == 'o'))




# import re;

# paths = open('14.txt').read().splitlines()


# rock_symbol = "#"
# air_symbol = '.'
# sand_symbol =  '+'

# rocks = set()
# sands = set()
# sand_start_coord = (500, 0)
# beach = set()

# range_sorted = lambda *p: range(min(p), max(p)+1)
# blocked = set()
# rocks_coords = []

# range_sorted = lambda *p: range(min(p), max(p)+1)
# blocked = set()

# for ps in [[*map(eval, line.split('->'))] for line in open('in.txt')]:
#     for (x1, y1), (x2, y2) in zip(ps, ps[1:]):
#         blocked |= {complex(x, y) for x in range_sorted(x1, x2)
#                                   for y in range_sorted(y1, y2)}

# floor = max(p.imag for p in blocked)
# part1, rock = 0, len(blocked)

# while 500 not in blocked: 
#     pos = 500
#     while True:
#         if pos.imag > floor:
#             if not part1: part1 = len(blocked)
#             break
#         for dest in pos+1j, pos-1+1j, pos+1+1j:
#             if dest not in blocked:
#                 pos = dest
#                 break
#         else: break
#     blocked.add(pos)

# print(part1-rock, len(blocked)-rock)


# lines_coords = [[[*map(int, c.split(','))] for c in l.split('->')] for l in open('14.txt')]
# lines_points_coords = set()


# coords_rocks = set()



# for line in lines_coords:
#     for (x1, y1), (x2, y2) in zip(line, line[1:]):

#         if x1 > x2:           # x2 must be the bigger one here
#             x1, x2 = x2, x1
#             y1, y2 = y2, y1

#         for i in range(int((x2-x1)/1) + 1):
#             x = x1 + i*1
#             y = (y1-y2)/(x1-x2) * (x - x1) + y1
#             print((x, y))


# def check_sand_options(coords):

#     if  (
#     #below
#     (coords[0], coords[1] + 1) in rocks or (coords[0], coords[1] + 1) in sands and 
#     #below-left
#     (coords[0] - 1, coords[1] + 1) in sands or (coords[0] - 1, coords[1] + 1) in rocks and  
#     #below-right
#     (coords[0] + 1, coords[1] + 1) in sands or (coords[0] + 1, coords[1] + 1) in rocks 
#     ):
#         return True
#     else:
#         return False

# def define_rocks(paths):
#     for line in paths:
#         rocks_coords.append([(int(a), int(b)) for a, b in (x.split(',') for x in re.findall("\d+,\d+", line))])
#     return rocks_coords

# def draw_beach(rocks, max_x, max_y):
#     for i in range(0, max_x):
#         for j in range(0, max_y):
#             if (i, j) in rocks:
#                 max_x = 1



# rocks = define_rocks(paths)
# max_x, max_y = max(rocks, key=lambda x: x[0])[0], max(rocks, key=lambda x: x[1])[1]


# draw_board = draw_beach(rocks, max_x[0], max_y[1])
