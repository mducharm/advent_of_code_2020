from shared.helper import get_input, chunk_by_blank_lines
from typing import Dict, List
import re

# Setup

data = get_input(__file__)

class Passport:

    def __init__(self, lines: List[str]) -> None:

        flattened_lines = [kvp for line in lines for kvp in line.split()]
        kvps = [(line.split(":")[0], line.split(":")[1]) for line in flattened_lines]

        self.fields: Dict[str, str] = dict(kvps)
        self.keys = self.fields.keys()

        self.field_validations = {
                "byr": self.byr,
                "iyr": self.iyr,
                "eyr": self.eyr,
                "hgt": self.hgt,
                "hcl": self.hcl,
                "ecl": self.ecl,
                "pid": self.pid
            }

        self.required_fields = self.field_validations.keys()

    def has_required_fields(self):
        return set(self.required_fields).issubset(set(self.fields.keys()))

    def byr(self):
        year = self.fields["byr"]
        if bool(re.search(r"^\d{4}$", year)):
            return int(year) > 1919 and int(year) < 2003
        else:
            return False

    def iyr(self):
        year = self.fields["iyr"]
        if bool(re.search(r"^\d{4}$", year)):
            return int(year) > 2009 and int(year) < 2021
        else:
            return False

    def eyr(self):
        year = self.fields["eyr"]
        if bool(re.search(r"^\d{4}$", year)):
            return int(year) > 2019 and int(year) < 2031
        else:
            return False

    def hgt(self):
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
        return bool(re.search(r"^(#[0-9a-fA-F]{6})$", self.fields["hcl"]))

    def ecl(self):
        return self.fields["ecl"] in "amb blu brn gry grn hzl oth".split()

    def pid(self):
        return bool(re.search(r"^([0-9]{9})$", self.fields["pid"]))

    def is_valid(self):
        if self.has_required_fields():
            results = [method() for (key, method) in self.field_validations.items() if key in self.keys]
            return all(results)
        
        return False


def get_passports(data: List[str]) -> List[Passport]:
    return [Passport(x) for x in chunk_by_blank_lines(data)]

# Problem 1

def problem_1():
    passports = get_passports(data)
    return sum(p.has_required_fields() for p in passports)

# Problem 2

def problem_2():
    passports = get_passports(data)
    return sum(p.is_valid() for p in passports)
