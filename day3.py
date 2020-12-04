import math
import timeit
from typing import List

test_data = open("day3_test_data.txt", "r").readlines()
data = open("day3_data.txt", "r").readlines()

# Problem 1

class SkiSlope:

    ground = "."
    tree = "#"
    
    def __init__(self, data) -> None:
        self.slope = [self.__convert_line(line) for line in data]

    def __convert_line(self, line):
        """
        Convert trees & ground to 0s and 1s
        """
        return [0 if c == self.ground else 1 for c in line if c in [self.tree, self.ground]]
    
    def count_trees(self, x, y) -> int:
        """
        Returns number of trees for a given path down the slope.
        """

        idx = 0
        current_line_idx = 0
        line_length = len(self.slope[0])
        total_lines = len(self.slope) - 1

        tree_count = 0

        while current_line_idx < total_lines:
            idx += x
            current_line_idx += y

            current_line = self.slope[current_line_idx]

            if idx >= line_length:
                idx -= line_length

            tree_count += current_line[idx]
            
        return tree_count


def problem_1_test():
    test_slope = SkiSlope(test_data)
    assert test_slope.count_trees(3, 1) == 7

def problem_1():
    return SkiSlope(data).count_trees(3, 1)

print(f"Problem 1 answer: {problem_1()}")

# Problem 2

coord_pairs = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

def problem_2_test():
    test_slope = SkiSlope(test_data)
    test_counts = [test_slope.count_trees(*coords) for coords in coord_pairs]
    assert math.prod(test_counts) == 336


def problem_2():
    answer_slope = SkiSlope(data)
    counts = [answer_slope.count_trees(*coords) for coords in coord_pairs]
    return math.prod(counts)

problem_2_test()

print(f"Problem 2 answer: {problem_2()}")

# Perf

iterations = 1000

duration = timeit.timeit(
    'problem_1()',
    'from __main__ import problem_1', 
    number=iterations)

print(f"Problem 1 (s): {duration / iterations:15.4f}")

duration2 = timeit.timeit(
    'problem_2()',
    'from __main__ import problem_2', 
    number=iterations)

print(f"Problem 2 (s): {duration2 / iterations:15.4f}")