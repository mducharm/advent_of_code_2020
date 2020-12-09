# Setup

from typing import Generator, List, Tuple
from itertools import product

test_data = [int(i) for i in open("day9_test_data.txt", "r").readlines()]
data = [int(i) for i in open("day9_data.txt", "r").readlines()]

Chunk = List[int]
NextNumber = int

def create_chunks(nums: List[int], preamble_size: int) -> Generator[Tuple[Chunk, NextNumber], None, None]:
    """
    Returns a generator for getting a slice of the provided nums based on the preamble size paired with the next number.

    Example item: ([35, 20, 15, 25, 47], 40)
    """
    return (
        (nums[x: x + preamble_size], x + preamble_size)
        for x in range(0, len(nums))
        if (x + preamble_size) < len(nums)
    )

def contains_valid_pair(current_num: int, chunk: List[int]):
    """
    Checks whether there is a pair of numbers in the provided chunk that add up to the current_num.
    """
    return any((current_num - x) in chunk for x in chunk)

def find_first_invalid_number(nums: List[int], preamble_size: int) -> int:
    chunks = create_chunks(nums, preamble_size)

    invalid_numbers = [nums[num_idx] for chunk,num_idx in chunks 
                                   if not contains_valid_pair(nums[num_idx], chunk)]

    return invalid_numbers[0]

# Problem 1

def problem_1_test():
    assert find_first_invalid_number(test_data, 5) == 127

def problem_1():
    return find_first_invalid_number(data, 25) 
    

problem_1_test()

print(f"Problem 1 answer: {problem_1()}")


# Problem 2

def get_possible_chunks(nums: List[int]) -> Generator[List[int], None, None]:
    num_range = range(len(nums))
    chunk_indexes = ((start,end) for start,end in product(num_range, num_range) if end > start + 1)
    possible_chunks = (nums[start:end] for start,end in chunk_indexes)

    return possible_chunks

def find_encryption_weakness(nums: List[int], invalid_num: int) -> int:

    invalid_num_idx = nums.index(invalid_num)

    nums_before = nums[0:invalid_num_idx]
    nums_after = nums[invalid_num_idx+1:]

    chunks_before = [min(chunk) + max(chunk) for chunk in get_possible_chunks(nums_before) if sum(chunk) == invalid_num]

    if len(chunks_before) > 0:
        return chunks_before[0]

    chunks_after = [min(chunk) + max(chunk) for chunk in get_possible_chunks(nums_after) if sum(chunk) == invalid_num]

    return chunks_after[0]


def problem_2_test():
    assert find_encryption_weakness(test_data, find_first_invalid_number(test_data, 5)) == 62

def problem_2():
    return find_encryption_weakness(data, find_first_invalid_number(data, 25))
    

problem_2_test()

print(f"Problem 2 answer: {problem_2()}")
