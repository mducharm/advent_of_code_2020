from day12.solutions import Direction, get_distance_with_waypoint, get_manhatten_distance
from shared.helper import get_input
import unittest

class Day_12_Tests(unittest.TestCase):


    def setUp(self) -> None:
        self.test_data = get_input(__file__, "input_test")

    def test_problem_1(self):
        self.assertTrue(get_manhatten_distance(self.test_data, (0, 0), Direction.East) == 25)

    def test_problem_2(self):

        self.assertTrue(get_distance_with_waypoint(self.test_data, (0, 0), Direction.East) == 286)


if __name__ == '__main__':
    unittest.main()
