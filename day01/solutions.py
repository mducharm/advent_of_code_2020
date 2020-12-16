import math
from shared.helper import get_input
from typing import List

file_1 = get_input(__file__)
file_data = [int(x) for x in file_1]

# Problem 1

def get_entries(data: List[int], expected_sum: int) -> List[int]:
    
    for num in data:
        if (expected_sum - num) in data:
            return [num, expected_sum - num]

    return [0, 0] # default if not found

def problem_1():
    return math.prod(get_entries(file_data, 2020))


# Problem 2

def get_three_entries(data: List[int], expected_sum: int) -> List[int]:

    for num in data:

        remaining = expected_sum - num

        possible_other_nums = filter(lambda x: x < remaining, data)

        for num2 in possible_other_nums:
            if (remaining - num2) in data:
                return [num, num2, remaining - num2]

    return [0, 0, 0] # default if not found


def problem_2():
    return math.prod(get_three_entries(file_data, 2020))
