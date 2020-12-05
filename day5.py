from dataclasses import dataclass
from typing import List
from itertools import product
# from collections import Counter

# Setup

@dataclass()
class Seat:
    # seat_position: str
    row: int
    column: int
    id: int

test_data = {
    "FBFBBFFRLR": Seat(44, 5, 357),
    "BFFFBBFRRR": Seat(70, 7, 567),
    "FFFBBBFRRR": Seat(14, 7, 119),
    "BBFFBBFRLL": Seat(102, 4, 820),
}

data = open("day5_data.txt", "r").readlines()

def binary_search(seat_position:str, upper: str, lower: str, remaining_seats: List[int]) -> int:
    if len(remaining_seats) > 1:
        midpoint = len(remaining_seats) // 2
        if seat_position[0] == upper:
            return binary_search(seat_position[1:], upper, lower, remaining_seats[midpoint:])
        else:
            return binary_search(seat_position[1:], upper, lower, remaining_seats[:midpoint])

    return remaining_seats[0]

def parse_seat_position(seat_position: str) -> Seat:

    row_partition = seat_position[:7]
    column_partition = seat_position[7:]

    rows = list(range(128))
    columns = list(range(8))

    row = binary_search(row_partition, "B", "F", rows)
    column = binary_search(column_partition, "R", "L", columns)
    id = row * 8 + column

    return Seat(row, column, id)

# Problem 1

def problem_1_test():
    for (seat_position, expected_seat) in test_data.items():
        actual_seat = parse_seat_position(seat_position)
        assert expected_seat == actual_seat

def problem_1():
    seats = [parse_seat_position(s) for s in data]

    highest_seat_id = -1

    for seat in seats:
        if seat.id > highest_seat_id:
            highest_seat_id = seat.id

    return highest_seat_id

problem_1_test()

print(f"Problem 1 answer: {problem_1()}")

# Problem 2


# def problem_2_old():
#     """
#     First convoluted answer, using columns & rows instead of ids...
#     """
    
#     filled_seats = [parse_seat_position(s) for s in data]

#     rows = Counter(x.row for x in filled_seats)
#     cols = Counter(x.column for x in filled_seats)

#     row_median = median(rows.keys())
#     col_median = median(cols.keys())

#     most_common_row_count = rows.most_common(1)[0][1]
#     most_common_col_count = cols.most_common(1)[0][1]

#     rows_with_missing_seats = [row for row,count in rows.items() if count != most_common_row_count]
#     cols_with_missing_seats = [col for col,count in cols.items() if count != most_common_col_count]

#     missing_row = sorted([(row, abs(row - row_median)) for row in rows_with_missing_seats], key=lambda x: x[1])[0][0]
#     missing_col = sorted([(col, abs(col - col_median)) for col in cols_with_missing_seats], key=lambda x: x[1])[0][0]

#     return missing_row * 8 + missing_col

def problem_2():

    existing_ids = {parse_seat_position(s).id for s in data}

    all_possible_ids = {(row * 8 + col) for row, col in product(range(128), range(8))}

    missing_ids = list(all_possible_ids - existing_ids)

    # get the first n where the difference between n and it's neighbors is greater than 1
    for id, count in enumerate(missing_ids):
        if missing_ids[count + 1] - id > 1:
            return missing_ids[count + 1]

print(f"Problem 2 answer: {problem_2()}")