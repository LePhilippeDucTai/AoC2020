import numpy as np
import functools as ft
import itertools as it

file = open("input.txt", "r")
data = [int(x.strip()) for x in file]
target = 2020

# Part 1
# Find the 2 integers that sum to 2020
def two_sum(data, target):
    x = np.array(data)
    solutions = list(set(target - x).intersection(set(data)))
    return np.prod(solutions)


# Part 2
# Find the 3 integers that sum to 2020
def three_sum(data, target):
    x = np.array(data)
    interm = [list(filter(lambda e: e >= 0, list(target - x - y))) for y in data]
    possible_solutions = list(set(it.chain(*interm)).intersection(data))
    return np.prod(possible_solutions)


print(two_sum(data, target))
print(three_sum(data, target))
