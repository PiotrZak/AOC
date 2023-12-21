import re

network = open("8.txt").read().splitlines()
direction = list(network[0])
network = {re.split(r"[\W]+", i)[0]: tuple(re.split(r"[\W]+", i)[1:]) for i in network[2:]}
start = "AAA"
finish = "ZZZ"
steps = 0
points = []


while True:
    for u in direction:
        steps += 1
        start = network[start][0] if u == "L" else network[start][1]
        current_point = points.append(network[start][0] if u == "L" else network[start][1])
        if start == finish:
            break
    else:
        continue
    break

print(steps)
print("This way took:", points)