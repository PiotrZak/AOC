import re, numpy

lines = [
"Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.",
"Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."
]

V = lambda *a: numpy.array(a)
k = lambda a: tuple(sum(a))

def parse(line):
    i,a,b,c,d,e,f = map(int, re.findall(r'\d+',line))
    return (i, (V(0,0,0,a), V(0,0,0,1)),     # Cost and production
               (V(0,0,0,b), V(0,0,1,0)),        # of each robot type,
               (V(0,0,d,c), V(0,1,0,0)),        # in the order geode,
               (V(0,f,0,e), V(1,0,0,0)),     # obs, clay, and ore.
               (V(0,0,0,0), V(0,0,0,0)))     # Construct no robot.

def run(blueprint, t):
    todo = [(V(0,0,0,0), V(0,0,0,1))]  # What we have and make.
    for _ in range(t):
        todo_ = list()                           # Queue for the next minute.
        for have, make in todo:
            for cost, more in blueprint:
                if all(have >= cost):         # We can afford this robot.
                    todo_.append((have+make-cost, make+more))
        todo = sorted(todo_, key=k)[-5000:]  # Prune the search queue.
    return max(todo, key=k)[0][0]

part1, part2 = 0, 1
for i, *blueprint in map(parse, open('19.txt')):
    part1 += run(blueprint, 24) * i
    part2 *= run(blueprint, 32) if i<4 else 1

print(part1, part2)


lines = [line.strip() for line in lines]

costs = list()
for line in lines: 
    # get all integers in line
    costs.append([int(i) for i in re.findall(r'\d+', line)])
#costs = [(1,4,2,3,14,2,7), (2,2,3,3,8,3,12)]    # Test example

def quality_heuristic(state): 
    # As the famous saying goes: 
    # 1 geode in the hand is worth 1000 in the bush
    minutes, (robots, inventory, mined) = state
    return 1000*mined[3] + 100*mined[2] + 10*mined[1] + mined[0]

def bfs(costs, robots, num_minutes, top_queue = 30000):
    queue = list()
    queue.append((0, (robots, (0,0,0,0), (0,0,0,0)))) # (minutes, (robots, inventory, mined))
    max_geodes_mined = 0
    depth = 0
    while queue:
        minutes, (robots, old_inventory, mined) = queue.pop(0)

        if minutes > depth: 
            # Prune our search space!!!
            queue.sort(key=quality_heuristic, reverse=True)
            queue = queue[:top_queue]
            depth = minutes

        if minutes == num_minutes:
            max_geodes_mined = max(max_geodes_mined, mined[3])
            continue
       
        # Mine ore with the robots
        new_inventory = tuple([old_inventory[i] + robots[i] for i in range(4)])
        new_mined = tuple([mined[i] + robots[i] for i in range(4)])
        
        # Case of not building a robot
        queue.append((minutes+1, (robots, new_inventory, new_mined)))

        # Build new robots, and try building each type of robot
        # TODO can we build more than one robot?
        for i in range(4):
            cost_robot = costs[i]

            # Check if we have enough materials to build a robot
            if all([old_inventory[j] >= cost_robot[j] for j in range(4)]): # We can build a robot!!
                new_robots = list(robots)
                new_robots[i] += 1
                new_robots = tuple(new_robots)

                new_inventory_state = tuple([new_inventory[j] - cost_robot[j] for j in range(4)])
                queue.append((minutes+1, (new_robots, new_inventory_state, new_mined)))
    return max_geodes_mined

max_minutes = 24
sum_quality = 0
# Part 1
# I used a simple queue, which was enough to find the optimal solution
# I prune everything too deep using the heuristic that having the higher up materials is better than the lower down materials
for blueprint_id, cost_ore_robot, cost_clay_robot, ob_ore, obs_clay, geode_ore, geode_ob in costs:
    cost_per_robot = [
        (cost_ore_robot, 0, 0, 0),
        (cost_clay_robot, 0, 0, 0),
        (ob_ore, obs_clay, 0, 0),
        (geode_ore, 0, geode_ob, 0)
    ]
    num_mined = bfs(cost_per_robot, (1,0,0,0), max_minutes, top_queue=1000)

    sum_quality += num_mined*blueprint_id
    print(f'Blueprint {blueprint_id}: {num_mined} geodes mined')
print("Part 1", sum_quality)

# Part 2
# We now compute for more minutes, but we need to multiply the number of geodes mined
# As the short queue I used in part 1 was not enough, I increased it to 10000
max_minutes = 32
product_geodes = 1
for blueprint_id, cost_ore_robot, cost_clay_robot, ob_ore, obs_clay, geode_ore, geode_ob in costs[:3]:
    cost_per_robot = [
        (cost_ore_robot, 0, 0, 0),
        (cost_clay_robot, 0, 0, 0),
        (ob_ore, obs_clay, 0, 0),
        (geode_ore, 0, geode_ob, 0)
    ]
    num_mined = bfs(cost_per_robot, (1,0,0,0), max_minutes, top_queue=10000)
    product_geodes *= num_mined
    print(f'Blueprint {blueprint_id}: {num_mined} geodes mined')
print("Part 2", product_geodes)


# import re

# minutes = 24
# robot_costs = []

# ore_robots = 0
# clay_robots = 0
# obsidian_robots = 0
# geode_robots = 0

# ore = 0
# clays = 0
# obsidian = 0
# geodes = 0

# demo = [
#     'robot_cost 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.',
# 'robot_cost 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.']

# for line in demo:
#     _, ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_obsidian = re.findall('\d+', line)
#     robot_costs.append((int(ore_cost), int(clay_cost), [int(obsidian_cost_ore), int(obsidian_cost_clay)], [int(geode_cost_ore), int(geode_cost_obsidian)]))

# # multiplying that robot_cost's ID number with the largest number of geodes that can be opened in 24 minutes using that robot_cost.


# def dfs (robot_cost):
#     pass


# for i in range(minutes):

#     ore += 1
#     print('minute', i)
#     print('resources:', ore, clays, obsidian, geodes)
    
#     for i, scenario in enumerate(robot_costs):
#         if i == 0:
#             ore_cost, clay_cost, obsidian_cost, geode_cost = scenario

#             if ore >= geode_cost[0] and obsidian >= geode_cost[1]:
#                 print('build geode robot')
#                 ore -= geode_cost[0]
#                 obsidian -= geode_cost[1]
#                 geode_robots += 1

#             if ore >= obsidian_cost[0] and clays >= obsidian_cost[1]:
#                 print('build obsidian robot')
#                 ore -= obsidian_cost[0]
#                 clays -= obsidian_cost[1]
#                 obsidian_robots += 1

#             if ore >= clay_cost:
#                 print('build clay robot')
#                 ore -= clay_cost
#                 clay_robots += 1

#             if ore >= ore_cost:
#                 print('build ore robot')
#                 ore -= ore_cost
#                 ore_robots += 1


    
#     if ore_robots > 0:
#         ore += ore_robots
    
#     if clay_robots > 0:
#         clays += clay_robots
    
#     if obsidian_robots > 0:
#         obsidian += obsidian_robots
    
#     if geode_robots > 0:
#         geodes += geode_robots

