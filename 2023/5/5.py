import re


with open('5test.txt', 'r') as f:
    lines = f.read().split('\n')

farm_data = {}

def parse_input(lines):

    maps = []
    current_map = []

    for line in lines:
        if not line:  # Empty line indicates a new map
            if current_map:
                maps.append(current_map)
                current_map = []
        else:
            current_map.append(line)

    if current_map:
        maps.append(current_map)

    return maps
farm_data = parse_input(lines) 

# print(farm_data[1:])
# print(farm_data[1:][0])

def match_seed_to_resources(seed, resources):

    print(resources)
    
    min_location = float('inf')
    for x in map(int, seeds):
        for resource in resources[1:]gi:
            for resource_coords in (resource[1:]):
                resource_coords = tuple(map(int, resource_coords.split()))
                d, s, r = resource_coords
                if x in range(s, s + r):
                    x += d - s
                    break

        min_location = min(x, min_location)
    return min_location
        

seeds = re.findall(r'\d+', farm_data[0][0])
seeds = [int(seed) for seed in seeds]


match_seed_to_resources(seeds, farm_data)
print(match_seed_to_resources(seeds, farm_data))


def acquirable_resources_coordination(resource):
    resources_ranges = []

    resource = [tuple(map(int, rule.split())) for rule in resource]
    # [(50, 97, 2)(52, 50,48)]
    for soil in resource:        
        d, s, r = soil

        destination_soil_list = (range(d, d + r))
        source_soil_list = (range(s, s + r))

        resources = {destination_soil_list, source_soil_list}
        resources_ranges.append(resources)

    return resources_ranges

soil, fertilizer, water, light, temperature, humidity, location = farm_data[1:]


soil_ranges = acquirable_resources_coordination(soil[1:])
## coords of soil
# print(acquirable_resources_coordination(soil[1:]))

# find the lowest location number that corresponds to any of the initial seeds

