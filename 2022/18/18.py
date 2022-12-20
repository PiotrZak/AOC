import re
figures = set()
not_connected = 0
touch_points = [
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1]
]
for line in open('18.txt').readlines():
    x,y,z = re.findall('\d+', line)
    figures.add((int(x), int(y), int(z)))
for x, y, z in figures:
    for ox, oy, oz in touch_points:
        if (int(x) + ox, int(y) + oy, int(z) + oz) not in figures:
            not_connected += 1
print(not_connected)
# from sys import stdin

# # Part 1
# (s:=open('18.txt').readlines()) and (u:={(i,*(c[k]+(i==k)*j for k in (0,1,2)))

#  for l in s for c in [[*map(int,l.split(','))]] 
#     for i in (0,1,2) 
#         for j in (0,1)}) and print(2*len(u)-6*len(s))


# def exposed_faces(cubes):
#     n_exposed = 0

#     for x, y, z in cubes:
#         for dx, dy, dz in (
#             (1, 0, 0),
#             (-1, 0, 0),
#             (0, 1, 0),
#             (0, -1, 0),
#             (0, 0, 1),
#             (0, 0, -1),
#         ):

#             if (x + dx, y + dy, z + dz) not in cubes:
#                 n_exposed += 1

#     return n_exposed


# def part1(s: str):
#     cubes = {tuple(int(val) for val in line.split(',')) for line in s.splitlines()}
#     return exposed_faces(cubes)


# import sys

# ## parse input
# lava = {tuple(map(int, line.split(","))) for line in open(sys.argv[1]).readlines()}

# ## Part 1
# def neighbors(xyz):
#     (x, y, z) = xyz
#     return {(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)}

# def num_lava_neighbors(xyz):
#     return sum(nxyz in lava for nxyz in neighbors(xyz))