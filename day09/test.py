from day09.solutions import find_encryption_weakness, find_first_invalid_number
from shared.helper import get_input
import unittest

class Day_09_Tests(unittest.TestCase):


    def setUp(self) -> None:
        self.test_data = [int(i) for i in get_input(__file__, "input_test")]

    def test_problem_1(self):
        self.assertTrue(find_first_invalid_number(self.test_data, 5) == 127)

    def test_problem_2(self):
        self.assertTrue(find_encryption_weakness(self.test_data, find_first_invalid_number(self.test_data, 5)) == 62)

if __name__ == '__main__':
    unittest.main()
