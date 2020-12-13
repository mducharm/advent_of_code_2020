
from typing import Generator, List


test_data = open("day13_test_data.txt", "r").readlines()
data = open("day13_data.txt", "r").readlines()

# Problem 1

def bus_departure_sequence(start: int, increment_by: int, limit: int) -> Generator[int, None, None]:
    num = start
    while True:
        if num < limit:
            yield num
            num += increment_by
        else:
            yield num

def get_earliest_bus_id(data: List[str]) -> int:

    earliest_timestamp = int(data[0])

    bus_ids = [int(id) for id in data[1].split(",") if id != "x"]

    start_time = 0

    departure_sequences = [(id, bus_departure_sequence(start_time, id, earliest_timestamp)) for id in bus_ids]

    earliest_id = 0 
    time_to_wait = 0

    while earliest_id == 0:

        next_sequence_values = [(id, next(sequence)) for id, sequence in departure_sequences]

        if all(next_time > earliest_timestamp for _, next_time in next_sequence_values):
            earliest_id, time = min(next_sequence_values, key=lambda t: t[1])
            time_to_wait = time - earliest_timestamp

    return earliest_id * time_to_wait


def problem_1_test():
    assert get_earliest_bus_id(test_data) == 295

def problem_1():
    return get_earliest_bus_id(data)

problem_1_test()

print(f"Problem 1: {problem_1()}")

