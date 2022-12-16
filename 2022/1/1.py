with open('1.txt', 'r') as f:
    elves = f.read().split('\n\n')

sums = []
# Part 1
for g in elves:
    elfs_calories = g.splitlines()
    print(elfs_calories)
    ints = list(map(int, elfs_calories))
    sumElves = sum(ints)
    sums.append(sumElves)

print(max(sums))

# Part 2
print(sum(sorted(sums)[-3:]))


# more elegant way

#p1
print(max(sum(int(line) for line in elf.splitlines()) for elf in elves))
#p2
print(sum(sorted([sum(int(line) for line in elf.splitlines()) for elf in elves])[-3:]))

