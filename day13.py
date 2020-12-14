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

# Problem 2

class Bus():

    def __init__(self, id: int, order: int) -> None:
        self.previous_stop_time = 0
        self.order = order
        self.id = id

        self.departure_generator = self._departure_time_gen(0, id)
        self.next_stop()

    def _departure_time_gen(self, start: int, increment_by: int) -> Generator[int, None, None]:
        """
        Returns a generator that increments by a given value indefinitely. 
        """
        num = start
        while True:
            yield num
            num += increment_by

    def next_stop(self):
        self.previous_stop_time = next(self.departure_generator)

def buses_are_sequential(buses: List[Bus]) -> bool:
    first_bus = buses[0]
    times = [bus.previous_stop_time - bus.order for bus in buses]
    return int(sum(times) / len(times)) == first_bus.previous_stop_time

def get_earliest_synced_time(data: List[str]) -> int:

    bus_ids = [int(id) if id != "x" else -1 for id in data[1].split(",")]

    # buses = [Bus(id, idx) for idx, id in enumerate(bus_ids) if id != -1]
    buses = [Bus(id, idx) for idx, id in enumerate(bus_ids) if id != -1]

    # for each bus, keep going until it gets to the next number divisible  

    for bus in buses:
        bus.next_stop()

    earliest_time = 0

    while earliest_time == 0:

        first_bus = buses[0]

        for bus in buses[1:]:
            while ((bus.previous_stop_time - bus.order) % first_bus.id) != 0 or ((first_bus.previous_stop_time + bus.order) > bus.previous_stop_time):
                bus.next_stop()

            while first_bus.previous_stop_time < (bus.previous_stop_time - bus.order):
                first_bus.next_stop()


        if buses_are_sequential(buses):
            earliest_time = first_bus.previous_stop_time

    return earliest_time


def problem_2_test():
    assert get_earliest_synced_time(["","17,x,13,19"]) == 3417 
    assert get_earliest_synced_time(test_data) == 1068781 

def problem_2():
    return get_earliest_synced_time(data) 

problem_2_test()

print(f"Problem 2: {problem_2()}")