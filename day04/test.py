from day04.solutions import get_passports
from shared.helper import get_input
from typing import List
import unittest

class Day_04_Tests(unittest.TestCase):

    test_data: List[str] 
    invalid_data: List[str] 
    valid_data: List[str] 

    def setUp(self) -> None:
        self.test_data = get_input(__file__, file_name="input_test")
        self.invalid_data = get_input(__file__, file_name="input_test_invalid")
        self.valid_data = get_input(__file__, file_name="input_test_valid")

    def test_problem_1(self):
        passports = get_passports(self.test_data)
        self.assertTrue(sum(p.has_required_fields() for p in passports) == 2)

    def test_problem_2(self):

        invalid_passports = get_passports(self.invalid_data)
        self.assertTrue(sum(p.is_valid() for p in invalid_passports) == 0)

        valid_passports = get_passports(self.valid_data)
        self.assertTrue(sum(p.is_valid() for p in valid_passports) == len(valid_passports))



if __name__ == '__main__':
    unittest.main()
