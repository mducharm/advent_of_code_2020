import timeit

file_1 = open("day2_data.txt", "r")
file_data = [x for x in file_1.readlines()]

# Problem 1

test_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


class Password:

    def __init__(self, s) -> None:
        policy, letter, password = s.split()

        self.character = letter[0]
        self.firstPolicyNum, self.secondPolicyNum = [int(n) for n in policy.split("-")]
        self.password = password
        self.character_count = password.count(self.character)

    def is_valid(self) -> bool:
        return self.character_count <= self.secondPolicyNum and self.character_count >= self.firstPolicyNum


def get_total_valid_passwords(data, password_class) -> int:
    valid_passwords = [password_class(s).is_valid() for s in data]

    return valid_passwords.count(True)


assert get_total_valid_passwords(test_data, Password) == 2




answer = get_total_valid_passwords(file_data, Password)
print(f"Problem 1 answer: {answer}")


# Problem 2

class PasswordWithNewPolicy(Password):

    def is_valid(self):
        first = self.password[self.firstPolicyNum - 1] == self.character 
        second = self.password[self.secondPolicyNum - 1] == self.character
        return first != second



assert get_total_valid_passwords(test_data, PasswordWithNewPolicy) == 1


answer2 = get_total_valid_passwords(file_data, PasswordWithNewPolicy)
print(f"Problem 2 answer: {answer2}")


# Perf

iterations = 1000
duration = timeit.timeit(
    'get_total_valid_passwords(file_data, Password)',
    'from __main__ import get_total_valid_passwords, file_data, Password', 
    number=1000)

print(f"Problem 1 (s): {duration / iterations:15.4f}")

duration2 = timeit.timeit(
    'get_total_valid_passwords(file_data, PasswordWithNewPolicy)',
    'from __main__ import get_total_valid_passwords, file_data, PasswordWithNewPolicy', 
    number=1000)

print(f"Problem 2 (s): {duration2 / iterations:15.4f}")