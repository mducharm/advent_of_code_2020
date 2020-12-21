from day10.solutions import get_all_possible_arrangements, get_jolt_differences
from shared.helper import get_input
import unittest

class Day_10_Tests(unittest.TestCase):


    def setUp(self) -> None:
        self.test_data_1 = [int(i) for i in get_input(__file__, "input_test_1")]
        self.test_data_2 = [int(i) for i in get_input(__file__, "input_test_2")]

    def test_problem_1(self):
        self.assertTrue(get_jolt_differences(self.test_data_1) == {1: 7, 3: 5})
        self.assertTrue(get_jolt_differences(self.test_data_2) == {1: 22, 3: 10})

    def test_problem_2(self):

        self.assertTrue(get_all_possible_arrangements(self.test_data_1) == 8)
        self.assertTrue(get_all_possible_arrangements(self.test_data_2) == 19208)

if __name__ == '__main__':
    unittest.main()
