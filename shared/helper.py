from typing import List
import os

def get_input(f: str, file_name: str = "input") -> List[str]:
    file_path = os.path.dirname(os.path.realpath(f))
    input_txt = open(file_path + f"\\{file_name}.txt", "r")
    return input_txt.readlines()

def chunk_by_blank_lines(data: List[str]) -> List[List[str]]:
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