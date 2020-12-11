from enum import Enum
from typing import  List
from itertools import product

test_data = [list(s.strip()) for s in open("day11_test_data.txt", "r").readlines()]
data = [list(s.strip()) for s in open("day11_data.txt", "r").readlines()]

class SeatStatus(Enum):
    Occupied = "#"
    Empty = "L"
    Floor = "."

AllSeats = List[List[SeatStatus]]

class Ferry():

    def __init__(self, data: List[List[str]]) -> None:

        seats: AllSeats = []

        for row in data:
            parsed_row: List[SeatStatus] = []
            for seat in row:
                parsed_row.append(SeatStatus(seat))
            
            seats.append(parsed_row)

        self.seats = seats
        self.seat_change_count = 0

    def __update_seats(self) -> None:
        new_seats: AllSeats = []

        for row_idx, row in enumerate(self.seats):
            new_row = []
            for col_idx, seat in enumerate(row):
                next_seat = self.__determine_next_seat_state(row_idx, col_idx, seat)
                new_row.append(next_seat)

            new_seats.append(new_row)

        self.seats = new_seats
        self.seat_change_count += 1
           

    def __determine_next_seat_state(self, row_idx: int, col_idx: int, current_seat: SeatStatus) -> SeatStatus:


        if current_seat == SeatStatus.Floor:
            return SeatStatus.Floor

        adjacent_seats = self.__get_adjacent_seats(row_idx, col_idx)

        if current_seat == SeatStatus.Empty:
            if not any(seat == SeatStatus.Occupied for seat in adjacent_seats):
                return SeatStatus.Occupied

        if current_seat == SeatStatus.Occupied:
            occupied_seats = adjacent_seats.count(SeatStatus.Occupied) 
            if occupied_seats >= 4:
                return SeatStatus.Empty

        return current_seat

    def __get_adjacent_seats(self, row_idx: int, col_idx: int) -> List[SeatStatus]:
    # def __get_adjacent_seats(self, row_idx: int, col_idx: int) -> Generator[SeatStatus, None, None]:

        adjacent_seats = (self.seats[x][y]
            for x,y in product([row_idx - 1, row_idx, row_idx + 1], [col_idx - 1, col_idx, col_idx + 1]) 
            if (x, y) != (row_idx, col_idx) 
            and 0 <= x < len(self.seats)
            and 0 <= y < len(self.seats[x])
        )

        return list(adjacent_seats)

    def __get_occupied_seat_count(self) -> int:
        return sum(seat == SeatStatus.Occupied for row in self.seats for seat in row)

    def __str__(self) -> str:
        return f"Iteration: {self.seat_change_count}\n" + "\n".join(
            "".join(seat.value for seat in row) for row in self.seats
            ) + "\n"


    def count_seats_once_stabilized(self) -> int:
        occupied_seat_count = []

        current_seat_count = self.__get_occupied_seat_count()

        while current_seat_count not in occupied_seat_count:
            self.__update_seats()
            occupied_seat_count.append(current_seat_count)
            current_seat_count = self.__get_occupied_seat_count()

        return current_seat_count



# Problem 1

def problem_1_test():
    assert Ferry(test_data).count_seats_once_stabilized() == 37

def problem_1():
    return Ferry(data).count_seats_once_stabilized()

problem_1_test()

print(f"Problem 1 answer: {problem_1()}")


# Problem 2

def problem_2_test():
    pass

def problem_2():
    pass

problem_2_test()

print(f"Problem 2 answer: {problem_2()}")
