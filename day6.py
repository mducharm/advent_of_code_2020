from typing import List
from collections import Counter


data = open("day6_data.txt", "r").readlines()

def separate_answers_into_groups(data: List[str]) -> List[List[str]]:
    """
    Chunks data from txt file by blank lines.
    """

    responses: List[List[str]] = []

    group_answers: List[str] = []

    for count, line in enumerate(data, start=1):

        blank_line = line.strip() == ""

        if not blank_line:
            group_answers.append(line.strip())

        if blank_line or count == len(data):
            responses.append(group_answers)
            group_answers = []

    return responses

# Problem 1

def get_answers_count(responses: List[str]) -> int:
    """
    Returns count of total unique answers found within a group's responses.
    """
    return len(set("".join(responses)))

def problem_1():
    return sum(get_answers_count(r) for r in separate_answers_into_groups(data))

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
    return sum(get_unison_answers_count(r) for r in separate_answers_into_groups(data))

print(f"Problem 2 answer: {problem_2()}")