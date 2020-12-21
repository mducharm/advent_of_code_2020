
from typing import List

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

def problem_1():
    return get_nth_number(data, 2020)

def problem_2():
    return get_nth_number(data, 30000000)
