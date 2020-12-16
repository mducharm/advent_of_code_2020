from day05.solutions import Seat, parse_seat_position
import unittest

class Day_05_Tests(unittest.TestCase):


    def setUp(self) -> None:
        self.test_data = {
            "FBFBBFFRLR": Seat(44, 5, 357),
            "BFFFBBFRRR": Seat(70, 7, 567),
            "FFFBBBFRRR": Seat(14, 7, 119),
            "BBFFBBFRLL": Seat(102, 4, 820),
        }

    def test_problem_1(self):
        for (seat_position, expected_seat) in self.test_data.items():
            actual_seat = parse_seat_position(seat_position)
            self.assertTrue(expected_seat == actual_seat)

if __name__ == '__main__':
    unittest.main()
