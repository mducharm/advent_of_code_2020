import math
import timeit
from typing import List

file_1 = open("day1_data.txt", "r")
file_data = [int(x) for x in file_1.readlines()]

# Problem 1

test_case = [1721, 979, 366, 299, 675, 1456]
test_numbers = [1721, 299]
test_answer = 514579

def get_entries(data: List[int], expected_sum: int) -> List[int]:
    
    for num in data:
        if (expected_sum - num) in data:
            return [num, expected_sum - num]

    return [0, 0] # default if not found

result = get_entries(test_case, 2020) 

assert result == test_numbers
assert math.prod(result) == test_answer

answer = math.prod(get_entries(file_data, 2020))
print(f"Problem 1 answer: {answer}")

# Problem 2

test_case = [1721, 979, 366, 299, 675, 1456]
test_numbers_2 = [979, 366, 675]
test_answer_2 = 241861950

def get_three_entries(data: List[int], expected_sum: int) -> List[int]:

    for num in data:

        remaining = expected_sum - num

        possible_other_nums = filter(lambda x: x < remaining, data)

        for num2 in possible_other_nums:
            if (remaining - num2) in data:
                return [num, num2, remaining - num2]

    return [0, 0, 0] # default if not found

result = get_three_entries(test_case, 2020)

assert result == test_numbers_2
assert math.prod(result) == test_answer_2

answer2 = math.prod(get_three_entries(file_data, 2020))
print(f"Problem 2 answer: {answer2}")


# Perf

iterations = 1000
duration = timeit.timeit(
    'get_entries(file_data, 2020)',
    'from __main__ import get_entries, file_data', 
    number=1000)

print(f"Problem 1 (s): {duration / iterations:15.7f}")

duration2 = timeit.timeit(
    'get_three_entries(file_data, 2020)',
    'from __main__ import get_three_entries, file_data', 
    number=1000)

print(f"Problem 2 (s): {duration2 / iterations:15.7f}")