import re

word_numbers = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('1.2test.txt', 'r') as f:
    lines = f.read().split('\n')

def get_digit(x):
    return x if x.isnumeric() else str(word_numbers.index(x))

total = 0
pattern = re.compile(r'(\d)')
pattern_words = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'  

for row in lines:
    digits = re.findall(pattern_words, row)
    total += int(get_digit(digits[0]) + get_digit(digits[-1]))
    print(total)

