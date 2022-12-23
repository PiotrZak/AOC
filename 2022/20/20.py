from collections import deque

input_file = list(map(int, open('20.txt', 'r').read().strip().split('\n')))
position_list = deque([(value, index) for index, value in enumerate(input_file)])

for i, num in enumerate(input_file):
    current_index = position_list.index((num, i))

    print(num)
    position_list.remove((num, i))
    position_list.rotate(-num)
    position_list.insert(current_index, (num, i))

final_list = list(map(lambda x: x[0], position_list))
zero_index = final_list.index(0)
print(sum(final_list[(zero_index+1000*i) % len(input_file)] for i in [1, 2, 3]))

# ___

nums = list(enumerate(x * 811589153 for x in map(int,open('in.txt').read().splitlines())))
n = len(nums)
pairs = nums[::] # Make a copy.
for _ in range(10):
    for pair in pairs:
        _, num = pair
        i = nums.index(pair)
        if num != 0:
            i = ((i + num - 1) % (n - 1)) + 1
        nums.remove(pair)
        nums.insert(i, pair)
nums = [v for _,v in nums]


m = nums.index(0)
a = nums[(m+1000) % n]
b = nums[(m+2000) % n]
c = nums[(m+3000) % n]
print(a+b+c)

# def swap(l, e):
#     i = l.index(e)
#     val, _ = l.pop(i)
#     iNew = (i+val)%len(l)
#     l.insert(iNew, e)    

# def mix(l, times = 1):
#     new = []
#     for i, n in enumerate(l):
#         new.append((n, i))
#     for _ in range(times):
#         for i, n in enumerate(l):
#             swap(new, (n, i))
#     return list(map(lambda x:x[0], new))

# with open('20.txt') as f:
#     items = list(map(str.strip, f.readlines()))
    
# l = list(map(int, items))
# mixed = mix(l)
# print(mixed)

# s = sum(mixed[(i+mixed.index(0))%len(mixed)] for i in (1000, 2000, 3000))
# print(s)

# dKey = 811589153
# l = list(map(lambda x:x*dKey, l))
# mixed = mix(l, 10)
# s = sum(mixed[(i+mixed.index(0))%len(mixed)] for i in (1000, 2000, 3000))
# print(s)