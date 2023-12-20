import re
from functools import reduce
import time

st = time.time()

with open('6.txt', 'r') as f:
    lines = f.read().split('\n')

races = [list(map(int, re.findall(r'\d+', line.split(":")[1]))) for line in lines if line]
time_distance_races_pairs = [list(pair) for pair in zip(*races)]

records_per_race = []

for i, race in enumerate(time_distance_races_pairs):

    milisecond,milimeter = race
    record = 0

    for hold in range(1, milisecond):
        distance = hold * (milisecond - hold)

        if distance > milimeter:
            record += 1

    records_per_race.append(record)

result = reduce(lambda x, y: x * y, records_per_race)
print(result)


et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

#P1: Execution time: 0.00019311904907226562 seconds
#P2: Execution time: 3.5336971282958984 seconds

#Since the current record for this race is 
#  9 millimeters, 
#  there are actually 4 different ways
#  you could win: you could hold the button
#  for 2, 3, 4, or 5 milliseconds
#  at the start of the race.


# holding the button (?)

# 3 races:
# Time:      7  15   30
# Distance:  9  40  200

#The first race lasts 7 milliseconds. The record distance in this race is 9 millimeters.



#determine the number of ways you can beat the record  in each race
