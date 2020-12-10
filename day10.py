
# Setup
from typing import Counter, Dict, List
import math

test_data_1 = [int(i) for i in open("day10_test_data1.txt", "r").readlines()]
test_data_2 = [int(i) for i in open("day10_test_data2.txt", "r").readlines()]
data = [int(i) for i in open("day10_data.txt", "r").readlines()]


JoltDifferences = Dict[int, int]

# Problem 1

def get_jolt_differences(data: List[int]) -> JoltDifferences:
    adapters = sorted(data)
    device = max(adapters) + 3
    jolt_diffs = test_adapters([*adapters, device], {}, 0)
    return jolt_diffs

def test_adapters(data: List[int], diffs: JoltDifferences, previous_jolt_rating: int) -> JoltDifferences:
    # base case 1
    if len(data) == 0:
        return diffs

    next_num, remaining_nums = data[0], data[1:]

    jolt_difference = next_num - previous_jolt_rating

    # base case 2
    if jolt_difference > 3:
        return diffs

    diffs[jolt_difference] = diffs.get(jolt_difference, 0) + 1

    return test_adapters(remaining_nums, diffs, next_num)


def problem_1_test():
    assert get_jolt_differences(test_data_1) == {1: 7, 3: 5}
    assert get_jolt_differences(test_data_2) == {1: 22, 3: 10}

def problem_1() -> int:
    diffs = get_jolt_differences(data)
    result: int = math.prod(diff for jolt, diff in diffs.items() if jolt in [1, 3])
    return result


problem_1_test()

print(f"Problem 1 answer: {problem_1()}")

# Problem 2

CombinationsPerNumber = Dict[int, int]

def get_combinations_per_number(data: List[int]) -> CombinationsPerNumber:
    """
    Returns a dictionary where keys represent each adapter, and values are the number of possible next adapters it can connect to
    """
    combination_counts: CombinationsPerNumber = {}

    sorted_data = sorted(data)

    for idx, num in enumerate(sorted_data):

        next_3_nums = sorted_data[idx + 1: idx + 4] if idx > 0 else sorted_data[1:4]

        combination_counts[num] = sum(1 for x in next_3_nums if x - num < 4)

        # if num == sorted_data[-1]:
        #     combination_counts[num] = num + 3 # last number will be guaranteed to have one path to device's jolt

    return combination_counts


def get_all_possible_arrangements(data: List[int]) -> int:

    combination_counts = get_combinations_per_number(data)

    x = sum(i for i in combination_counts.values() if i > 1) + 1
    return x

    # counts = count_possible_paths(data, 0, combination_counts)

    # result = math.prod(counts) / len(counts)

    # return result

# def count_possible_paths(data: List[int], count: int, combination_counts: CombinationsPerNumber) -> int:

#     if len(data) == 0:
#         return count

#     c = count


#     for idx, num in enumerate(data):
#         possible_next_nums = combination_counts.get(num)
#         c += count_possible_paths(data[idx:], 0, possible_next_nums)

#     return count



def problem_2_test():
    assert get_all_possible_arrangements(test_data_1) == 8
    assert get_all_possible_arrangements(test_data_2) == 19208

def problem_2():
    return get_all_possible_arrangements(data) 

problem_2_test()

print(f"Problem 2 answer: {problem_2()}")
