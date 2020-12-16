from typing import List
from shared.helper import get_input

file_1 = get_input(__file__)
file_data = [x for x in file_1]

# Problem 1

class Password:

    def __init__(self, s: str) -> None:
        policy, letter, password = s.split()

        self.character = letter[0]
        self.firstPolicyNum, self.secondPolicyNum = [int(n) for n in policy.split("-")]
        self.password = password
        self.character_count = password.count(self.character)

    def is_valid(self) -> bool:
        return self.character_count <= self.secondPolicyNum and self.character_count >= self.firstPolicyNum


def get_total_valid_passwords(data: List[str], password_class) -> int:
    valid_passwords = [password_class(s).is_valid() for s in data]

    return valid_passwords.count(True)


def problem_1():
    return get_total_valid_passwords(file_data, Password)


# Problem 2

class PasswordWithNewPolicy(Password):

    def is_valid(self):
        first = self.password[self.firstPolicyNum - 1] == self.character 
        second = self.password[self.secondPolicyNum - 1] == self.character
        return first != second


def problem_2():
    return get_total_valid_passwords(file_data, PasswordWithNewPolicy)
