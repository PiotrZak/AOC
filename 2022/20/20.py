def swap(l, e):
    i = l.index(e)
    val, _ = l.pop(i)
    iNew = (i+val)%len(l)
    l.insert(iNew, e)    

def mix(l, times = 1):
    new = []
    for i, n in enumerate(l):
        new.append((n, i))
    for _ in range(times):
        for i, n in enumerate(l):
            swap(new, (n, i))
    return list(map(lambda x:x[0], new))

with open('20.txt') as f:
    items = list(map(str.strip, f.readlines()))
    
l = list(map(int, items))
mixed = mix(l)
print(mixed)

s = sum(mixed[(i+mixed.index(0))%len(mixed)] for i in (1000, 2000, 3000))
print(s)

dKey = 811589153
l = list(map(lambda x:x*dKey, l))
mixed = mix(l, 10)
s = sum(mixed[(i+mixed.index(0))%len(mixed)] for i in (1000, 2000, 3000))
print(s)