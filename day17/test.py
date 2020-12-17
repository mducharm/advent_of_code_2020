from day17.solutions import cycle_cubes
from shared.helper import get_input
import unittest

class Day_17_Tests(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = get_input(__file__, "input_test")

    def test_problem_1(self):
        # cubes = ConwayCubes(self.test_data)

        # cubes.run_boot_process(6)

        # active_cubes = cubes.get_num_of_active_cubes()
        result = cycle_cubes(self.test_data, 6)

        self.assertEqual(result, 112)

    def test_problem_2(self):
        pass


if __name__ == '__main__':
    unittest.main()
