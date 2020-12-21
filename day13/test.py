from day13.solutions import get_earliest_bus_id, get_earliest_synced_time
from shared.helper import get_input
import unittest

class Day_13_Tests(unittest.TestCase):


    def setUp(self) -> None:
        self.test_data = get_input(__file__, "input_test")

    def test_problem_1(self):
        self.assertTrue(get_earliest_bus_id(self.test_data) == 295)

    def test_problem_2(self):

        self.assertTrue(get_earliest_synced_time(["","17,x,13,19"]) == 3417)
        self.assertTrue(get_earliest_synced_time(self.test_data) == 1068781)



if __name__ == '__main__':
    unittest.main()
