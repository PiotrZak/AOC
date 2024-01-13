total = 0

def _hash(_s: str):
    h: int = 0
    for i in _s:
        h = (h + ord(i)) * 17 % 256
    return h

for step in open("15.txt").readline().strip().split(','):
    v = 0
    v = _hash(step)
    total += v
print(total)

