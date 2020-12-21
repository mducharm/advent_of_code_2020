
# Setup
from typing import Dict, List
from shared.helper import get_input
import math

data = [int(i) for i in get_input(__file__)]


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


def problem_1() -> int:
    diffs = get_jolt_differences(data)
    result: int = math.prod(diff for jolt, diff in diffs.items() if jolt in [1, 3])
    return result


# Problem 2

def get_all_possible_arrangements(data: List[int]) -> int:

    nums = sorted(data)

    counts = {
        0: 1
    }

    for num in nums:
        counts[num] = sum(counts.get(num - x, 0) for x in range(1, 4))

    return counts[nums[-1]]
   

def problem_2():
    return get_all_possible_arrangements(data) 
