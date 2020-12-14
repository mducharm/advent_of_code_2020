from typing import List
import re


test_data = open("day14_test_data.txt", "r").readlines()
data = open("day14_data.txt", "r").readlines()

# Problem 1

def process_docking_data(data: List[str]) -> int:

    mask = ""
    total = {}

    while data:

        next_line = data[0]

        new_mask = re.search(r"^mask = (?P<mask>[0-1X]{36})", next_line)

        if new_mask:
            mask = new_mask.group("mask") 
            data = data[1:]
            continue

        next_value = re.search(r"^mem\[(?P<mem>[0-9]+)\] = (?P<value>[0-9]+)", next_line)

        if next_value:
            mem, value = next_value.group("mem"), int(next_value.group("value"))

            value |= int(mask.replace("X", "0"), base=2) # flip ones from mask
            value &= int(mask.replace("X", "1"), base=2) # flip zeroes from mask

            total[mem] = value

        data = data[1:]

    return sum(total.values())


def problem_1_test():
    assert process_docking_data(test_data) == 165


def problem_1():
    return process_docking_data(data)

problem_1_test()

print(f"Problem 1 answer: {problem_1()}")

def problem_2_test():
    assert process_docking_data(test_data) == 165


def problem_2():
    return process_docking_data(data)

problem_2_test()

print(f"Problem 2 answer: {problem_2()}")