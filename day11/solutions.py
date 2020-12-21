from enum import Enum
from typing import List
from itertools import product
from shared.helper import get_input

data = [list(s.strip()) for s in get_input(__file__)]

class SeatStatus(Enum):
    Occupied = "#"
    Empty = "L"
    Floor = "."

AllSeats = List[List[SeatStatus]]


# Problem 1

class FerryProblem1():

    def __init__(self, data: List[List[str]]) -> None:

        seats: AllSeats = []

        for row in data:
            parsed_row: List[SeatStatus] = []
            for seat in row:
                parsed_row.append(SeatStatus(seat))
            
            seats.append(parsed_row)

        self.seats = seats
        self.seat_change_count = 0
        self.seat_limit = 4

    def _update_seats(self) -> None:
        new_seats: AllSeats = []

        for row_idx, row in enumerate(self.seats):
            new_row = []
            for col_idx, seat in enumerate(row):
                next_seat = self._determine_next_seat_state(row_idx, col_idx, seat)
                new_row.append(next_seat)

            new_seats.append(new_row)

        self.seats = new_seats
        self.seat_change_count += 1
           

    def _determine_next_seat_state(self, row_idx: int, col_idx: int, current_seat: SeatStatus) -> SeatStatus:

        if current_seat == SeatStatus.Floor:
            return SeatStatus.Floor

        adjacent_seats = self._get_adjacent_seats(row_idx, col_idx)

        if current_seat == SeatStatus.Empty:
            if not any(seat == SeatStatus.Occupied for seat in adjacent_seats):
                return SeatStatus.Occupied

        if current_seat == SeatStatus.Occupied:
            occupied_seats = adjacent_seats.count(SeatStatus.Occupied) 
            if occupied_seats >= self.seat_limit:
                return SeatStatus.Empty

        return current_seat

    def _get_adjacent_seats(self, row_idx: int, col_idx: int) -> List[SeatStatus]:
        """
        Returns the statuses of all adjacent seats.
        """
        return [self.seats[x][y]
            for x,y in product([row_idx - 1, row_idx, row_idx + 1], [col_idx - 1, col_idx, col_idx + 1]) 
            if (x, y) != (row_idx, col_idx) 
            and 0 <= x < len(self.seats)
            and 0 <= y < len(self.seats[x])
        ]

    def _get_occupied_seat_count(self) -> int:
        return sum(seat == SeatStatus.Occupied for row in self.seats for seat in row)

    def __str__(self) -> str:
        return f"Iteration: {self.seat_change_count}\n" + "\n".join(
            "".join(seat.value for seat in row) for row in self.seats
            ) + "\n"


    def count_seats_once_stabilized(self) -> int:
        occupied_seat_count = []

        current_seat_count = self._get_occupied_seat_count()

        while current_seat_count not in occupied_seat_count:
            self._update_seats()
            occupied_seat_count.append(current_seat_count)
            current_seat_count = self._get_occupied_seat_count()

        return current_seat_count



def problem_1():
    return FerryProblem1(data).count_seats_once_stabilized()

class FerryProblem2(FerryProblem1):

    def __init__(self, data: List[List[str]]) -> None:
        super().__init__(data)

        self.seat_limit = 5

    def _get_adjacent_seats(self, row_idx: int, col_idx: int) -> List[SeatStatus]:
        """
        Returns the statuses of all seats that can be seen from the current seat.
        """

        adjacent_seats = []

        possible_increments = product([-1, 1, 0], [-1, 1, 0])
        
        row_length = len(self.seats) - 1
        col_length = len(self.seats[0]) - 1

        for dx_dy in possible_increments:

            if dx_dy == (0,0):
                continue

            x, y = row_idx, col_idx
            dx, dy = dx_dy

            x += dx
            y += dy

            while 0 <= x <= row_length and 0 <= y <= col_length:

                next_seat = self.seats[x][y]

                if next_seat != SeatStatus.Floor:
                    adjacent_seats.append(next_seat)
                    break

                x += dx
                y += dy

        return adjacent_seats

def problem_2():
    return FerryProblem2(data).count_seats_once_stabilized()
