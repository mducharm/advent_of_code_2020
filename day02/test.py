from day02.solutions import Password, PasswordWithNewPolicy, get_total_valid_passwords
import unittest

class Day_02_Tests(unittest.TestCase):

    test_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

    def test_problem_1(self):

        results = get_total_valid_passwords(self.test_data, Password)

        self.assertEqual(results, 2)

    def test_problem_2(self):

        results = get_total_valid_passwords(self.test_data, PasswordWithNewPolicy)

        self.assertEqual(results, 1)


if __name__ == '__main__':
    unittest.main()
