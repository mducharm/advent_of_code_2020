from day14.solutions import process_docking_data, process_docking_data_v2
from shared.helper import get_input
import unittest

class Day_14_Tests(unittest.TestCase):


    def setUp(self) -> None:
        self.test_data = get_input(__file__, "input_test")
        self.test_data_2 = get_input(__file__, "input_test_2")

    def test_problem_1(self):
        self.assertTrue(process_docking_data(self.test_data) == 165)

    def test_problem_2(self):
        self.assertTrue(process_docking_data_v2(self.test_data_2) == 208)



if __name__ == '__main__':
    unittest.main()
