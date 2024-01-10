file = open("./14.txt").readlines()

reflector = tuple(line.strip() for line in file)

# (O) - rounded rock
#  #  - flat rock
# . - empty space
# https://en.wikipedia.org/wiki/Transpose

def transpose(matrix):
    return list(map("".join, zip(*matrix)))

# flip reflector
reflector = transpose(reflector)

for i, row in enumerate(reflector):
    groups = []
    # sort reflector by splitting #
    for group in row.split("#"):
        new_group = sorted(tuple(group), reverse=True)
        groups.append("".join(new_group))

    reflector[i] = "#".join(groups)

# flip reflector back
reflector = transpose(reflector)

count = 0

for i, row in enumerate(reversed(reflector)):
    count += row.count("O") * (i + 1)

print(count)