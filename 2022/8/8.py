lines = open('8.txt').read().splitlines()
# trees = []
# for y, row in enumerate(lines):
#     trees.append(list(map(int,row)))

# visibles = 0
# for i, row in enumerate(trees):
#     for j, element in enumerate(row):

#         print('i: ', i, 'j: ', j, 'element: ', element)

#         top    = (element > r[j] for r in trees[:i])
#         left   = (element > c    for c in row[:j])
#         right  = (element > c    for c in row[j + 1:])
#         bottom = (element > r[j] for r in trees[i + 1:])
#         if any([all(top), all(left), all(right), all(bottom)]):
#             visibles += 1

# print(visibles)

# INPUT_FILE = 'input.txt'


# def main():
#     with open(INPUT_FILE, 'r') as file:
#         trees = tuple([tuple(map(int, list(row.strip())))
#                        for row in file.read().strip().split()])

#     scores = []

#     for i, row in enumerate(trees):
#         for j, col in enumerate(row):
#             element = trees[i][j]

#             top = tuple(reversed([element > row[j] for row in trees[:i]]))
#             left = tuple(reversed([element > col for col in trees[i][:j]]))
#             right = tuple([element > col for col in trees[i][j + 1:]])
#             bottom = tuple([element > row[j] for row in trees[i + 1:]])

#             to_top = \
#                 top.index(False) + 1 if (False in top) else len(top)
#             to_left = \
#                 left.index(False) + 1 if (False in left) else len(left)
#             to_right = \
#                 right.index(False) + 1 if (False in right) else len(right)
#             to_bottom = \
#                 bottom.index(False) + 1 if (False in bottom) else len(bottom)

#             score = to_top * to_left * to_right * to_bottom
#             scores.append(score)

#     print(max(scores))


# if __name__ == '__main__':
#     main()x


# solution by Alex Telon:


grid = []
for y, row in enumerate(lines):
    grid.append(list(map(int,row)))
# Transposes the grid.
cols = list(zip(*grid))

print(cols)
pointsNumbers = 0

def views(x,y):
    """Returns the view in the 4 directions from a given position.
    The order is defined as in aoc. above, left, right, below
    Also they are ordered as seen from the (x,y) coordinate.
    """
    above = cols[x][:y]
    left  = grid[y][:x]
    right = grid[y][x+1:]
    below = cols[x][y+1:]
    return [above[::-1], left[::-1], right, below]
    
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        cords = views(x,y)
        print(cords)

print(pointsNumbers)