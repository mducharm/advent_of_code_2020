from shared.helper import get_input
from day07.solutions import count_bags_containing_gold_bag, parse_luggage_rules, total_bags
import unittest

class Day_07_Tests(unittest.TestCase):


    def setUp(self) -> None:
        self.test_data = get_input(__file__, "input_test")
        self.test_data_2 = get_input(__file__, "input_test_2")

    def test_problem_1(self):
        rules = parse_luggage_rules(self.test_data)
        count = count_bags_containing_gold_bag(rules)
        self.assertTrue(count == 4)

    def test_problem_2(self):
        count = total_bags(parse_luggage_rules(self.test_data_2))
        self.assertTrue(count == 126)

if __name__ == '__main__':
    unittest.main()
