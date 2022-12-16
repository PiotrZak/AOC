
common = 0
commonPairs=0

with open('4.txt', 'r') as f:
    lines = f.read().splitlines()
    
for s in lines:
    a, b = s.split(',')
    a = a.split('-')
    b = b.split('-')

    aRange = (list(range(int(a[0]), int(a[1])+1)))
    bRange = (list(range(int(b[0]), int(b[1])+1)))

    if set(aRange).issubset(set(bRange)):
        #p1
        common += 1

    elif set(bRange).issubset(set(aRange)):
        common += 1

    #p2
    commonPairs += any(set(aRange).intersection(set(bRange)))
