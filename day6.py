from typing import List
from collections import Counter
from helper import chunk_by_blank_lines

data = open("day6_data.txt", "r").readlines()

# Problem 1

def get_answers_count(responses: List[str]) -> int:
    """
    Returns count of total unique answers found within a group's responses.
    """
    return len(set("".join(responses)))

def problem_1():
    return sum(get_answers_count(r) for r in chunk_by_blank_lines(data))

print(f"Problem 1 answer: {problem_1()}")

# Problem 2

def get_unison_answers_count(responses: List[str]) -> int:
    """
    Returns count of responses answered by each individual in a group. 
    """
    num_of_people = len(responses)
    counts = Counter("".join(responses))
    answered_by_everyone = [val for val in counts.values() if val == num_of_people]
    return len(answered_by_everyone)

def problem_2():
    return sum(get_unison_answers_count(r) for r in chunk_by_blank_lines(data))

print(f"Problem 2 answer: {problem_2()}")