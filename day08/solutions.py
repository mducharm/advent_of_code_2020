from typing import List, Tuple
from shared.helper import get_input

data = get_input(__file__)

Instructions = List[Tuple[str, int]]

def parse_instructions(data: List[str]) -> Instructions:
    instructions = (instruction.split(" ") for instruction in data)
    return [(instruction[0], int(instruction[1])) for instruction in instructions]

# Problem 1

def apply_operation(instruction: Tuple[str, int], idx: int, acc: int) -> Tuple[int, int]:
    """
    Returns new index and accumulated count based on the provided instruction.
    """
    op, param = instruction
    return (
        idx + param if op =="jmp" else idx + 1,
        acc + param if op == "acc" else acc
    )

def run_instructions(instructions: Instructions) -> Tuple[int, bool]:
    visited_indexes = []
    idx = 0
    acc = 0

    while idx not in visited_indexes and idx != len(instructions):

        visited_indexes.append(idx)

        idx, acc = apply_operation(instructions[idx], idx, acc)

    terminates = idx == len(instructions) 

    return acc, terminates

def problem_1():
    acc, _ = run_instructions(parse_instructions(data)) 
    return acc

# Problem 2

def flip_instruction(instruction: Tuple[str, int]) -> Tuple[str, int]:
    op, parameter = instruction
    if op == "jmp":
        return ("nop", parameter) 
    else: 
        return ("jmp", parameter)

def find_terminating_instructions_amount(instructions: Instructions) -> int:

    results: List[Tuple[int, bool]] = []

    for idx, instruction in enumerate(instructions):
        op = instruction[0]

        if op in ["jmp", "nop"]:
            modified_instructions = instructions[:]
            modified_instructions[idx] = flip_instruction(instruction)
            results.append(run_instructions(modified_instructions))

    return next(acc for acc,terminates in results if terminates)

def problem_2():
    result = find_terminating_instructions_amount(parse_instructions(data))
    return result
