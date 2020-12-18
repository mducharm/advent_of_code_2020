from day18.solutions import process_math_problem
import unittest

class Day_18_Tests(unittest.TestCase):

    def setUp(self) -> None:
        self.test_cases = [
            ("2 * 3 + (4 * 5)", 26),
            ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
            ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
            ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632)
        ]

        self.test_cases_2 = [
            ("1 + (2 * 3) + (4 * (5 + 6))", 51),
            ("2 * 3 + (4 * 5)", 46),
            ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
            ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
            ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340)
        ]

    def test_problem_1(self):
        for exp, expected_result in self.test_cases:
            actual_result = process_math_problem(exp)

            self.assertEqual(expected_result, actual_result)
            


    def test_problem_2(self):
        pass



if __name__ == '__main__':
    unittest.main()
