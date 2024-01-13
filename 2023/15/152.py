from typing import List, Dict

def _hash(_s: str):
    h: int = 0
    for i in _s:
        h = (h + ord(i)) * 17 % 256
    return h

with open('15.txt') as file:
    sequence: List[str] = file.read().split(',')

boxes: Dict[int, Dict[str, int]] = {i: {} for i in range(256)}

for op in sequence:
    if op[-2] == '=':
        s, v = op.split('=')
        boxes[_hash(s)][s] = int(v)
    elif op[-1] == '-':
        s: str = op[:-1]
        hsh: int = _hash(s)
        if s in boxes[hsh]:
            del boxes[hsh][s]


print(sum(sum(m * v * i for i, v in enumerate(box.values(), 1)) for m, box in enumerate(boxes.values(), 1)))