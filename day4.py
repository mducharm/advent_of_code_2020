from typing import Dict, List
import re

# Setup

test_data = open("day4_test_data.txt", "r").readlines()
data = open("day4_data.txt", "r").readlines()

invalid_data = open("day4_problem2_invalid.txt", "r").readlines()
valid_data = open("day4_problem2_valid.txt", "r").readlines()

class Passport:

    required_fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]

    optional_fields = ["cid"]

    def __init__(self, lines) -> None:

        flattened_lines = [kvp for line in lines for kvp in line.split()]
        kvps = [(line.split(":")[0], line.split(":")[1]) for line in flattened_lines]

        self.fields: Dict[str, str] = dict(kvps)
        self.keys = self.fields.keys()

    def has_required_fields(self):
        return set(self.required_fields).issubset(set(self.fields.keys()))

    def byr(self):
        if "byr" not in self.keys:
            return False

        y = self.fields["byr"]
        if bool(re.search(r"^\d{4}$", y)):
            return int(y) > 1919 and int(y) < 2003
        else:
            return False

    def iyr(self):
        if "iyr" not in self.keys:
            return False

        y = self.fields["iyr"]
        if bool(re.search(r"^\d{4}$", y)):
            return int(y) > 2009 and int(y) < 2021
        else:
            return False

    def eyr(self):
        if "eyr" not in self.keys:
            return False

        y = self.fields["eyr"]
        if bool(re.search(r"^\d{4}$", y)):
            return int(y) > 2019 and int(y) < 2031
        else:
            return False

    def hgt(self):
        if "hgt" not in self.keys:
            return False

        height = self.fields["hgt"]
        if "cm" in height:
            results = re.search(r"^(\d\d\d)cm$", height)

            if results == None:
                return False

            num = results.group(1)
            return int(num) >= 150 and int(num) <= 193
        elif "in" in height:
            results = re.search(r"^(\d\d)in$", height)

            if results == None:
                return False

            num = results.group(1)
            return int(num) >= 59 and int(num) <= 76
        else:
            return False

    def hcl(self):
        if "hcl" not in self.keys:
            return False

        color = self.fields["hcl"]
        return bool(re.search(r"^(#[0-9a-fA-F]{6})$", color))

    def ecl(self):
        if "ecl" not in self.keys:
            return False

        return self.fields["ecl"] in "amb blu brn gry grn hzl oth".split()

    def pid(self):
        if "pid" not in self.keys:
            return False

        return bool(re.search(r"^([0-9]{9})$", self.fields["pid"]))

    def is_valid(self):
        validation_methods = [getattr(self, x) for x in self.required_fields]
        validations = [x() for x in validation_methods]

        if self.has_required_fields():
            return all(validations)
        
        return False


def parse_data(data: List[str]) -> List[Passport]:

    passport_data: List[List[str]] = []

    current_passport: List[str] = []

    for count, line in enumerate(data, start=1):

        if line.strip() == "":
            passport_data.append(current_passport)
            current_passport = []
        elif count == len(data):
            current_passport.append(line)
            passport_data.append(current_passport)
            current_passport = []
        else:
            current_passport.append(line)

    return [Passport(x) for x in passport_data]


# Problem 1

def problem_1_test():
    passports = parse_data(test_data)
    assert sum(p.has_required_fields() for p in passports) == 2

def problem_1():
    passports = parse_data(data)
    return sum(p.has_required_fields() for p in passports)

problem_1_test()

print(f"Problem 1 answer: {problem_1()}")


# Problem 2

def problem_2_test():
    invalid_passports = parse_data(invalid_data)
    assert sum(p.is_valid() for p in invalid_passports) == 0

    valid_passports = parse_data(valid_data)
    assert sum(p.is_valid() for p in valid_passports) == len(valid_passports)

def problem_2():
    passports = parse_data(data)
    return sum(p.is_valid() for p in passports)

problem_2_test()

print(f"Problem 2 answer: {problem_2()}")