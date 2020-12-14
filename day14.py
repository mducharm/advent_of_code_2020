from typing import Generator, List, Tuple
import re
from itertools import product


test_data = open("day14_test_data.txt", "r").readlines()
test_data2 = open("day14_test_data2.txt", "r").readlines()
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

# Problem 2

def process_docking_data_v2(data: List[str]) -> int:

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
            memory_address, value = int(next_value.group("mem")), int(next_value.group("value"))

            # initial overwrite of ones:
            memory_address |= int(mask.replace("X", "0"), base=2)

            memory_addresses: List[int] = []

            # Generate every possible sequence of 0s and 1s that could fill the Xs
            possible_combinations = (xs for xs in product([0, 1], repeat=mask.count("X")))

            for combination in possible_combinations:
                # Like first problem, isolate values that need to change (the Xs) and remove extraneous numbers that have already been processed in the mask (0s and 1s)
                temp_mask = mask.replace("0", "_").replace("1", "_")

                for num in combination:
                    temp_mask = temp_mask.replace("X", str(num), 1)

                memory_address |= int(temp_mask.replace("_", "0"), base=2) # flip ones from mask
                memory_address &= int(temp_mask.replace("_", "1"), base=2) # flip zeroes from mask

                memory_addresses.append(memory_address)

            for mem in memory_addresses:
                total[mem] = value

        data = data[1:]

    return sum(total.values())

def problem_2_test():
    assert process_docking_data_v2(test_data2) == 208


def problem_2():
    return process_docking_data_v2(data)

problem_2_test()

print(f"Problem 2 answer: {problem_2()}")