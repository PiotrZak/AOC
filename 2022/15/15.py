import re
 
scan_row = 2000000
non_beacons = set()
 
discs = []
 

def calc_sensors_range_coords(sensors):

    sensors_range = []
    for sensor in sensors:
        x, y, r = sensor

        top = (x, y + r)
        right = (x + r, y)
        bottom = (x, y - r)
        left =  (x - r, y)

        radar_visability = set()

        for x in range (left[0], right[0]+1):
            for y in range (bottom[1], top[1]+1):
                radar_visability.add((x, y))
        
        sensors_range.append(radar_visability)
    return sensors_range


def construct_map(s, b, flatten_sensors_range):

    max_y = max(max(y for _,y,_ in s), max(y for _,y in b))
    max_x = max(max(x for x,_,_ in s), max(x for x,_ in b))

    min_y = min(min(y for _,y,_ in s), min(y for _,y in b))
    min_x = min(min(x for x,_,_ in s), min(x for x,_ in b))

    sensors_coords = [(x, y) for x, y, _ in s]
    sensors_radius = [r for _, _, r in s]
    
    for y in range (min_y, max_y+1):
        for x in range (min_x, max_x+1):

            if (x, y) in sensors_coords:
                print("S", end='')
            elif (x, y) in b:
                print("B", end='')
            else:
                if (x, y) in flatten_sensors_range:
                    print("#", end='')
                else:
                    print(".", end='')
        print('.\n')

sensors = set()
beacons = set()

with open('15-test.txt', 'r') as f:
    for line in f.readlines():
        sx, sy, bx, by = (int(z[1:]) for z in re.findall(r'=-?\d+', line))

        sensors.add((sx, sy))
        beacons.add((bx, by))
        radius = abs(bx-sx) + abs(by-sy)
        discs.append((sx, sy, radius))
 
        # dist_to_scan_row = abs(scan_row - sy)
        # num_steps_left = radius - dist_to_scan_row
 
        # if num_steps_left < 0:
        #     continue
 
        # for x in range(sx - num_steps_left, sx + num_steps_left + 1):
        #     pos = (x, scan_row)
        #     if pos != (bx, by):
        #         non_beacons.add(pos)

sensors_range = calc_sensors_range_coords(discs)
flatten_sensors_range = [food for sublist in sensors_range for food in sublist]

construct_map(discs, beacons, flatten_sensors_range)


#print("part 1:", len(non_beacons))
 
# def get_boundary(x, y, r):
#     temp = (x, y+r)
#     while temp != (x+r, y):
#         temp = (temp[0]+1, temp[1]-1)
#         yield temp
#     while temp != (x, y-r):
#         temp = (temp[0]-1, temp[1]-1)
#         yield temp
#     while temp != (x-r, y):
#         temp = (temp[0]-1, temp[1]+1)
#         yield temp
#     while temp != (x, y+r):
#         temp = (temp[0]+1, temp[1]+1)
#         yield temp
 
# # part 2
# for x, y, r in discs:
#     print("disc {} {} {}".format(x, y, r))
#     for px, py in get_boundary(x, y, r+1):
#         if 0 <= px <= 4000000 and 0 <= py <= 4000000:
#             for dx, dy, dr in discs:
#                 if (abs(px-dx) + abs(py-dy)) <= dr:
 
#                     break
#             else:
#                 print("beacon:", px, py)
#                 print("tuning freq:", 4000000 * px + py)
#                 break
 