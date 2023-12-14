import math as m, re
import time

st = time.time()

board = list(open('3.txt'))
coords_chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    
    # object with coords -> eg. <re.Match object; span=(63, 66), match='318'>
    for n in re.finditer(r'\d+', row):

    # this is coords of edge of number:
    # xxxxx
    # x343x 
    # xxxxx
    # in this case 12 edges (x, y)

        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

    # (100, 28): [940]
    # key = (100, 28)
    # value = 940

    # checking if number is adjacent to symbol
        for o in edge & coords_chars.keys():
            coords_chars[o].append(int(n.group()))

print(sum(sum(p)    for p in coords_chars.values()),
      sum(m.prod(p) for p in coords_chars.values() if len(p)==2))


et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
#Execution time: 0.005763053894042969 seconds