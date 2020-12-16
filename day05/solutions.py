from dataclasses import dataclass
from typing import List
from itertools import product
from enum import Enum
from shared.helper import get_input

# Setup

@dataclass()
class Seat:
    row: int
    column: int
    id: int

data = get_input(__file__)

class Partition(Enum):
    upper = 1
    lower = 2

def binary_search(partitions: List[Partition], seats: List[int]) -> int:
    if len(seats) > 1:
        mid = len(seats) // 2

        next_partition, remaining_partitions = partitions[0], partitions[1:]

        upper, lower = seats[mid:], seats[:mid]

        if next_partition is Partition.upper:
            return binary_search(remaining_partitions, upper)
        else:
            return binary_search(remaining_partitions, lower)

    return seats[0]

def as_partitions(s: str, upper: str) -> List[Partition]:
    return [Partition.upper if char == upper else Partition.lower for char in list(s)]

def parse_seat_position(seat_position: str) -> Seat:

    row_partition = as_partitions(seat_position[:7], "B")
    column_partition = as_partitions(seat_position[7:], "R")

    rows = list(range(128))
    columns = list(range(8))

    row = binary_search(row_partition, rows)
    column = binary_search(column_partition, columns)
    id = row * 8 + column

    return Seat(row, column, id)

# Problem 1

def problem_1():
    seats = [parse_seat_position(s) for s in data]

    highest_seat_id = -1

    for seat in seats:
        if seat.id > highest_seat_id:
            highest_seat_id = seat.id

    return highest_seat_id

# Problem 2

def problem_2():

    existing_ids = {parse_seat_position(s).id for s in data}

    all_possible_ids = {(row * 8 + col) for row, col in product(range(128), range(8))}

    missing_ids = list(all_possible_ids - existing_ids)

    # get the first n where the difference between n and it's neighbors is greater than 1
    for id, count in enumerate(missing_ids):
        if missing_ids[count + 1] - id > 1:
            return missing_ids[count + 1]
