import math
from day01.solutions import get_entries, get_three_entries
import unittest

class Day_01_Tests(unittest.TestCase):

    test_case = [1721, 979, 366, 299, 675, 1456]
    test_numbers = [1721, 299]
    test_answer = 514579

    test_numbers_2 = [979, 366, 675]
    test_answer_2 = 241861950

    def test_problem_1(self):

        result = get_entries(self.test_case, 2020) 

        self.assertEqual(result, self.test_numbers)
        self.assertEqual(math.prod(result), self.test_answer)

    def test_problem_2(self):

        result = get_three_entries(self.test_case, 2020)

        self.assertEqual(result, self.test_numbers_2)
        self.assertEqual(math.prod(result), self.test_answer_2)
        
    

if __name__ == '__main__':
    unittest.main()
