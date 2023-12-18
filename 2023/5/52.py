#  4HbQ - author

from functools import reduce

seeds, *mappings = open('5test.txt').read().split('\n\n')
seeds = map(int, seeds.split()[1:])


def lookup(start, mapping):
    print(start)
    for m in mapping.split('\n')[1:]:
        dst, src, len = map(int, m.split())
        delta = start - src
        if delta in range(len):
            return dst + delta
    else: return start

[82, 43, 86, 35]
print(min(reduce(lookup, mappings, int(s)) for s in seeds))