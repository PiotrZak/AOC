import re
import time
import numpy as np

st = time.time()

with open('1test.txt', 'r') as f:
    lines = f.read().split('\n')

total = 0 

# note - problematic with the regex, had problem with scanning number and separate it into digits instead get digits

# r'(\d)' - r'(\d)' matches a single digit and captures it.
#          e.g. ['4', '9', '8', '9']

# r'\d+' - matches one or more consecutive digits
#          without capturing them as a group.
#          e.g. [4989]

# Combine the regex pattern and compile it for better performance
pattern = re.compile(r'(\d)')

for row in lines:
    numbers = pattern.findall(row)
    if numbers:
        total += int(numbers[0] + numbers[-1])

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

#Execution time: 0.0001881122589111328 seconds