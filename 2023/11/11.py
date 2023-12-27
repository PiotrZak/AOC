
#shortest path between every pair of galaxies
with open('11test.txt', 'r') as f:
    lines = f.read().split('\n')

def find_galaxies(lines):
    galaxies = [(i, j) for i, line in enumerate(lines) for j, char in enumerate(line) if char == '#']
    space = [(i, j) for i, line in enumerate(lines) for j, char in enumerate(line) if char != '#']

    return galaxies, space

def find_empty_spaces(lines):
    empty_rows = [i for i, line in enumerate(lines) if all(char != '#' for char in line)]
    
    # Transpose the lines to find empty columns
    transposed_lines = list(map(list, zip(*lines)))
    empty_cols = [j for j, col in enumerate(transposed_lines) if all(char != '#' for char in col)]

    return empty_rows, empty_cols



galaxies, space = find_galaxies(lines)
x, y = find_empty_spaces(lines)


def get_galaxy_pairs(galaxies):
    galaxy_pairs = []

    for i, (galaxy_row, galaxy_col) in enumerate(galaxies):
        for (other_galaxy_row, other_galaxy_col) in galaxies[:i]:
            galaxy_pairs.append(((galaxy_row, galaxy_col), (other_galaxy_row, other_galaxy_col)))

    return galaxy_pairs

def shortest_path_between_pairs(galaxy_pairs):
    
    shortest_path = 0

    for (galaxy_row, galaxy_col), (other_galaxy_row, other_galaxy_col) in galaxy_pairs:
        for row in range(min(other_galaxy_row, galaxy_row), max(other_galaxy_row, galaxy_row)):
            shortest_path += 2 if row in x else 1

        for col in range(min(other_galaxy_col, galaxy_col), max(other_galaxy_col, galaxy_col)):
            shortest_path += 2 if col in y else 1

    return shortest_path

print(get_galaxy_pairs(galaxies))
print(len(get_galaxy_pairs(galaxies)))
print(shortest_path_between_pairs(get_galaxy_pairs(galaxies)))