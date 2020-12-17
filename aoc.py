import unittest
import sys
import importlib
import webbrowser

if __name__ == '__main__':

    day = sys.argv[1]
    day = day if len(day) == 2 else "0" + day
    if len(sys.argv) == 2:

        module = importlib.import_module(f"day{day}.solutions")
        
        problem_1 = getattr(module, "problem_1")
        problem_2 = getattr(module, "problem_2")

        print(f"Problem 1 answer: {problem_1()}")
        print(f"Problem 2 answer: {problem_2()}")

    if len(sys.argv) == 3 and sys.argv[2] == "test":
        module = importlib.import_module(f"day{day}.test")

        test_class = getattr(module, f"Day_{day}_Tests")

        suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_class)
        unittest.TextTestRunner(verbosity=2).run(suite)

    if len(sys.argv) == 3 and sys.argv[2] == "open":

        webbrowser.open_new_tab(f"https://adventofcode.com/2020/day/{day}")






