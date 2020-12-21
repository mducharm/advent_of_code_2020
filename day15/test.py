from day15.solutions import get_nth_number
import unittest

class Day_15_Tests(unittest.TestCase):


    def setUp(self) -> None:

        self.tests = [
            ([0, 3, 6], 436),
            ([1, 3, 2], 1),
            ([2, 1, 3], 10),
            ([1, 2, 3], 27),
            ([2, 3, 1], 78),
            ([3, 2, 1], 438),
            ([3, 1, 2], 1836),
        ]

        self.tests_pt2 = [
            ([0, 3, 6], 175594),
            ([1, 3, 2], 2578),
            ([2, 1, 3], 3544142),
            ([1, 2, 3], 261214),
            ([2, 3, 1], 6895259),
            ([3, 2, 1], 18),
            ([3, 1, 2], 362),
        ]


    def test_problem_1(self):

        for data, answer in self.tests:
            result = get_nth_number(data, 2020)
            self.assertTrue(result == answer)


    def test_problem_2(self):
        for data, answer in self.tests_pt2:
            result = get_nth_number(data, 30000000)
            self.assertTrue(result == answer)



if __name__ == '__main__':
    unittest.main()
