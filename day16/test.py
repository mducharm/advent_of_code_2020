from day16.solutions import get_rule_positions, get_ticket_scanning_error_rate
from shared.helper import get_input
import unittest

class Day_16_Tests(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = get_input(__file__, "input_test")
        self.test_data_2 = get_input(__file__, "input_test_2")

    def test_problem_1(self):
        self.assertEqual(get_ticket_scanning_error_rate(self.test_data), 71)

    def test_problem_2(self):

        rule_positions, _ = get_rule_positions(self.test_data_2)

        expected_positions = {
            "row": 0,
            "class": 1,
            "seat": 2,
        }

        self.assertEqual(rule_positions, expected_positions)


if __name__ == '__main__':
    unittest.main()
