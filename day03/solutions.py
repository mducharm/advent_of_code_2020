import math
from typing import List
from shared.helper import get_input

data: List[str] = get_input(__file__)

# Problem 1

class SkiSlope:

    ground = "."
    tree = "#"
    
    def __init__(self, data: List[str]) -> None:
        self.slope = [self.__convert_line(line) for line in data]

    def __convert_line(self, line: str):
        """
        Convert trees & ground to 0s and 1s
        """
        return [0 if c == self.ground else 1 for c in line if c in [self.tree, self.ground]]
    
    def count_trees(self, x: int, y: int) -> int:
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

def problem_1():
    return SkiSlope(data).count_trees(3, 1)


# Problem 2

coord_pairs = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

def problem_2():
    answer_slope = SkiSlope(data)
    counts = [answer_slope.count_trees(*coords) for coords in coord_pairs]
    return math.prod(counts)
