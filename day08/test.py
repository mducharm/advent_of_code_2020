from day08.solutions import find_terminating_instructions_amount, parse_instructions, run_instructions
from shared.helper import get_input
import unittest

class Day_08_Tests(unittest.TestCase):


    def setUp(self) -> None:
        self.test_data = get_input(__file__, "input_test")

    def test_problem_1(self):
        acc, _ = run_instructions(parse_instructions(self.test_data)) 
        self.assertTrue(acc == 5)

    def test_problem_2(self):
        result = find_terminating_instructions_amount(parse_instructions(self.test_data))
        self.assertTrue(result == 8)

if __name__ == '__main__':
    unittest.main()
