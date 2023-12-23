#pascal triangle
# 1str1ker1 solution
#notice the next element is the sum of the previous elements multiplied by their corresponding position in a binomial expansion (pascal's triangle)

# https://en.wikipedia.org/wiki/Pascal%27s_triangle


# Import math Library
# import math

# # Initialize the number of items to choose from
# n = 7

# # Initialize the number of possibilities to choose
# k = 5

# # Print total number of possible combinations
# print (math.comb(n, k)) -> 21


from math import comb

with open("9.txt", "r") as file:
    lines = file.readlines()
    total_sum = 0

    for line in lines:
        formatted_line = line.split()

        for index, value in enumerate(formatted_line):
            pascal = comb(len(formatted_line), index)
            total_sum += int(value) * pascal * (-1) ** (len(formatted_line) - index + 1)

    print(f"total: {total_sum}")