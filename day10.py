
# Setup
from typing import Dict, List
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

def get_all_possible_arrangements(data: List[int]) -> int:

    nums = sorted(data)

    counts = {
        0: 1
    }

    for num in nums:
        counts[num] = sum(counts.get(num - x, 0) for x in range(1, 4))

    return counts[nums[-1]]
   

def problem_2_test():
    assert get_all_possible_arrangements(test_data_1) == 8
    assert get_all_possible_arrangements(test_data_2) == 19208

def problem_2():
    return get_all_possible_arrangements(data) 

problem_2_test()

print(f"Problem 2 answer: {problem_2()}")
