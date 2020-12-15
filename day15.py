
from typing import List
import time

tests = [
    ([0, 3, 6], 436),
    ([1, 3, 2], 1),
    ([2, 1, 3], 10),
    ([1, 2, 3], 27),
    ([2, 3, 1], 78),
    ([3, 2, 1], 438),
    ([3, 1, 2], 1836),
]

tests_pt2 = [
    ([0, 3, 6], 175594),
    ([1, 3, 2], 2578),
    ([2, 1, 3], 3544142),
    ([1, 2, 3], 261214),
    ([2, 3, 1], 6895259),
    ([3, 2, 1], 18),
    ([3, 1, 2], 362),
]

data = [13,16,0,12,15,1]


def turn_gen(start: int, increment_by: int):
    num = start
    while True:
        yield num
        num += increment_by

def get_nth_number(data: List[int], limit: int) -> int:

    num_counter = {
        number: [turn_spoken]
        for turn_spoken, number in enumerate(data, 1)
    }

    current_turn = len(data) + 1
    last_num_spoken: int = data[-1] # 6

    turns = turn_gen(current_turn + 1, 1)

    while current_turn <= limit:

        num_of_times_spoken = len(num_counter.get(last_num_spoken, []))

        if num_of_times_spoken <= 1:
            last_num_spoken = 0
        else:
            last_num_spoken = num_counter[last_num_spoken][-1] - num_counter[last_num_spoken][-2]

        num_counter[last_num_spoken] = num_counter.get(last_num_spoken, [])[-1:] + [current_turn]

        current_turn = next(turns)

    return last_num_spoken

# Problem 1

def problem_1_test():
    for idx, (data, answer) in enumerate(tests):
        result = get_nth_number(data, 2020)
        passes = result == answer

        if passes:
            print(f"Test {idx} passed.")
        else:
            print(f"Test {idx} failed with answer {result} instead.")


def problem_1():
    return get_nth_number(data, 2020)

problem_1_test()

t0 = time.time()
print(f"Problem 1 answer: {problem_1()}")
t1 = time.time()
print(t1 - t0)

# Problem 2

def problem_2_test():

    for idx, (data, answer) in enumerate(tests_pt2):
        result = get_nth_number(data, 30000000)
        passes = result == answer

        if passes:
            print(f"Test {idx} passed.")
        else:
            print(f"Test {idx} failed with answer {result} instead.")


def problem_2():
    return get_nth_number(data, 30000000)

# problem_2_test()

t0 = time.time()
print(f"Problem 2 answer: {problem_2()}")
t1 = time.time()
print(t1 - t0)