# solution - by morgoth1145, zawerf, and others
#https://github.com/morgoth1145/advent-of-code/blob/2bf7c157e37b3e0a65deedc6c88e42297d813d1d/2022/16/solution.py
#The relevant search space can be formulated as "which is the next valve to turn off"
#precalculate the distances between all nodes with non-zero flow rate
#While recursively searching, keep track of which nodes have been turned off and remove those from next options
#Keep track of the current best score achieved - if it is no longer possible to beat this score, end the current recursion early

import collections as c, itertools, functools, re
import re

valves = tuple()
D = c.defaultdict(lambda: 1000)

for line in open('16-test.txt').readlines():
    words = line.split()
    valves_symbols = []
    for i, word in enumerate(words):
        if i == 0:
            flow_rate = re.findall('\d+', line)
            valves_symbols.extend(flow_rate)
        without_comma = word.replace(',', '')
        if len(without_comma) == 2 and without_comma != 'to':
            valves_symbols.append(without_comma) 
            
    valves += (valves_symbols, )

#print (valves)


r = r'Valve (\w+) .*=(\d*); .* valves? (.*)'

V, F, D = set(), dict(), c.defaultdict(lambda: 1000)

for v, f, us in re.findall(r, open('16-test.txt').read()):

    V.add(v)                                  # store node
    if f != '0': F[v] = int(f)                # store flow
    for u in us.split(', '): D[u,v] = 1       # store dist

for k, i, j in itertools.product(V, V, V):    # floyd-warshall
    D[i,j] = min(D[i,j], D[i,k] + D[k,j])

print (F)

@functools.cache
def search(t, u='AA', vs=frozenset(F), e=False):

    return max([F[v] * (t-D[u,v]-1) + search(t-D[u,v]-1, v, vs-{v}, e)
           for v in vs if D[u,v]<t] + [search(26, vs=vs) if e else 0])

print(search(30), search(26, e=True))




# import re
# from collections import defaultdict

# graph = {}
# rates = {}
# for line in open("16-test.txt").read().strip().split("\n"):
#     front, back = re.split(r"; tunnels? leads? to valves? ", line)
#     x = front.split(" ")[1]
#     rates[x] = int(front.split("=")[-1])
#     graph[x] = back.split(", ")

# print(rates)
# print(graph)

# nodeId = defaultdict(lambda: len(nodeId))
# [nodeId[u] for u in rates if rates[u]]  # only assign consecutive ids to non-zero rates
# print([nodeId[u] for u in rates if rates[u]] )
# ALL_MASK = (1 << len(nodeId)) - 1

# print(ALL_MASK)

# cache = defaultdict(lambda: [[-1 for mask in range(ALL_MASK + 1)] for t in range(31)])

# def dp(u, t, mask):
#     if t == 0:
#         return 0
#     if cache[u][t][mask] == -1:
#         best = max(dp(v, t - 1, mask) for v in graph[u])
#         bit = 1 << nodeId[u]
#         if bit & mask:
#             best = max(best, dp(u, t - 1, mask - bit) + rates[u] * (t - 1))
#         cache[u][t][mask] = best


#     return cache[u][t][mask]

# print("Part1", dp("AA", 30, ALL_MASK))
# print("Part2", max(dp("AA", 26, ALL_MASK - mask) + dp("AA", 26, mask) for mask in range(ALL_MASK + 1)))

