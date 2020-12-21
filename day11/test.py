from day11.solutions import FerryProblem1, FerryProblem2
from shared.helper import get_input
import unittest

class Day_11_Tests(unittest.TestCase):


    def setUp(self) -> None:
        self.test_data = [list(s.strip()) for s in get_input(__file__, "input_test")]

    def test_problem_1(self):
        self.assertTrue(FerryProblem1(self.test_data).count_seats_once_stabilized() == 37)

    def test_problem_2(self):
        self.assertTrue(FerryProblem2(self.test_data).count_seats_once_stabilized() == 26)


if __name__ == '__main__':
    unittest.main()
