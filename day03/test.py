import math
from shared.helper import get_input
from typing import List
from day03.solutions import SkiSlope, coord_pairs
import unittest

class Day_03_Tests(unittest.TestCase):

    test_data: List[str] 

    def setUp(self) -> None:
        self.test_data = get_input(__file__, file_name="input_test")

    def test_problem_1(self):

        test_slope = SkiSlope(self.test_data)
        results = test_slope.count_trees(3, 1) 

        self.assertEqual(results, 7)

    def test_problem_2(self):

        test_slope = SkiSlope(self.test_data)
        test_counts = [test_slope.count_trees(*coords) for coords in coord_pairs]
        self.assertEqual(math.prod(test_counts), 336)


if __name__ == '__main__':
    unittest.main()
