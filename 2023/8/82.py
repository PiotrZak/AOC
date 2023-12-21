import re
import math

def read_input(filename):
    return open(filename).read().splitlines()

input_list = read_input("8.txt")
direction, node_dict = list(input_list[0]), {k: (v1, v2) for k, v1, v2, *_ in (re.split(r"[\W]+", i) for i in input_list[2:])}
ghost_list = [key for key in node_dict if key.endswith("A")]
steps, max_steps = 0, 1
math_list, loop_list = [""] * len(ghost_list) * 2, [""] * len(ghost_list)


while True:
    for u in direction:
        steps += 1

        for i, p in enumerate(ghost_list):
            if p.endswith("Z") and math_list[i] != "" and loop_list[i] == "":
                loop_list[i] = steps - math_list[i + len(ghost_list)]
                
            if p.endswith("Z") and math_list[i] == "":
                math_list[i], math_list[i + len(ghost_list)] = p, steps

            node_tuple = node_dict[p]
            ghost_list[i] = node_tuple[0] if u == "L" else node_tuple[1]

        if "" not in loop_list:
            #print(math.lcm(*map(int, loop_list)))
            exit()