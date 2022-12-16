from string import ascii_lowercase as lc
lines = open('12.txt').read().splitlines()

climb_limit = 2
max_x = 40
max_y = 161

def get_neighbors(x, y, nodes: dict):
    neighbors = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for dx, dy in neighbors:
        if (0 <= x + dx <= max_x) and (0 <= y + dy <= max_y):
            if nodes[(x + dx, y + dy)] - nodes[(x, y)] < climb_limit:
                yield x + dx, y + dy

def generate_map():
    # point = {z: (x, y)}
    point = dict()
    a_points = list()
    start = (0, 0)
    end = (0, 0)
    for x, line in enumerate(lines):
        for y, z in enumerate(line):
            if z == 'S':
                start = (x, y)
            if z == 'E':
                end = (x, y)
            if z == 'a':
                a_points.append((x, y))
            point[(x, y)] = lc.index(z) if z in lc else {"E": 25, "S": 0}[z]
    return point, start, end, a_points

def deep_first_search(nodes, start, destination):
    visited = {start: 0}
    queue = [start]
    while queue:
        node = queue.pop(0)
        current_step = visited[node]
        for dx, dy in get_neighbors(*node, nodes):
            if (dx, dy) == destination:
                return current_step + 1
            if (dx, dy) not in visited:
                queue.append((dx, dy))
                visited[(dx, dy)] = current_step + 1

def djisktra_algorithm(nodes, start, destination):
    # initialize the distance to infinity
    distance = {node: float('inf') for node in nodes}
    # initialize the previous node to None
    previous = {node: None for node in nodes}
    # initialize the distance to 0 for the start node
    distance[start] = 0
    # initialize the queue with the start node
    queue = [start]
    # while the queue is not empty
    while queue:
        # get the node with the smallest distance
        current_node = min(queue, key=lambda node: distance[node])
        # remove the current node from the queue
        queue.remove(current_node)
        # if the current node is the destination, return the distance
        if current_node == destination:
            return distance[destination]
        # for each neighbor of the current node
        for neighbor in get_neighbors(*current_node, nodes):
            # calculate the distance to the neighbor
            distance_to_neighbor = distance[current_node] + 1
            # if the distance to the neighbor is smaller than the current distance
            if distance_to_neighbor < distance[neighbor]:
                # update the distance to the neighbor
                distance[neighbor] = distance_to_neighbor
                # update the previous node of the neighbor
                previous[neighbor] = current_node
                # add the neighbor to the queue
                queue.append(neighbor)

map, start, dest, a_points = generate_map()
print(djisktra_algorithm(map, start, dest))
print(deep_first_search(map, start, dest))

#p2
print(min(filter(None, [deep_first_search(map, s, dest) for s in a_points])))




# import sys, collections

# def solve(grid, *start):
#     Q = collections.deque((i, j, 0, 'a') for i in range(len(grid)) 
#                     for j in range(len(grid[0])) 
#                     if grid[i][j] in start)
#     visited = set((i, j) for i, j, _, _ in Q)

#     def push(i, j, d, a):
#         if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])): return
#         if (i, j) in visited: return
#         b = grid[i][j].replace('E', 'z')
#         if ord(b) > ord(a) + 1: return
#         visited.add((i, j))
#         Q.append((i, j, d + 1, b))

#     while len(Q):
#         i, j, d, a = Q.popleft()
#         if grid[i][j] == 'E': return d
#         push(i + 1, j, d, a)
#         push(i - 1, j, d, a)
#         push(i, j + 1, d, a)
#         push(i, j - 1, d, a)

# grid = sys.stdin.read().splitlines()
# print(solve(grid, 'S'), solve(grid, 'S', 'a'))