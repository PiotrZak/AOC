# author mgtezak


import re

with open('5test.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    segments = puzzle_input.split('\n\n')
    seeds = re.findall(r'\d+', segments[0])

    print(segments)

    min_location = float('inf')
    for x in map(int, seeds):
        for seg in segments[1:]:
            for conversion in re.findall(r'(\d+) (\d+) (\d+)', seg):
                destination, start, delta = map(int, conversion)
                if x in range(start, start + delta):
                    x += destination - start
                    break

        min_location = min(x, min_location)

    return min_location

print(part1(puzzle_input))