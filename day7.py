from typing import Dict, List
import re
# Setup

test_data = open("day7_test_data.txt", "r").readlines()
data = open("day7_data.txt", "r").readlines()

LuggageRules = Dict[str, Dict[str, int]]

def parse_luggage_rules(data: List[str]) -> LuggageRules:
    rules: LuggageRules = {}

    for rule in data:

        bag, child_bags = rule.replace("bags", "bag").replace(".", "").strip().split(" contain ")

        if child_bags == "no other bags":
            rules[bag] = {}
        else:
            contained_bags = {}

            for child in re.finditer(r"(\d)\s(\w+\s\w+\s\w+)", child_bags):
                bag_name, amount = child.group(2), child.group(1)
                contained_bags[bag_name] = int(amount)

            rules[bag] = contained_bags

    return rules

def bag_contains_gold_bag(bag: str, rules: LuggageRules) -> bool:

    inner_bags = rules[bag].keys()

    if len(inner_bags) == 0:
        return False

    if "shiny gold bag" in inner_bags:
        return True
    
    return any(bag_contains_gold_bag(child, rules) for child in inner_bags)


def count_bags_containing_gold_bag(rules: LuggageRules) -> int:
    bags = rules.keys()
    return sum(bag_contains_gold_bag(b, rules) for b in bags)

# Problem 1

def problem_1_test():
    rules = parse_luggage_rules(test_data)
    count = count_bags_containing_gold_bag(rules)
    assert count == 4

def problem_1():
    rules = parse_luggage_rules(data)
    count = count_bags_containing_gold_bag(rules)
    return count

problem_1_test()

print(f"Problem 1 answer: {problem_1()}")

# Problem 2

test_data2 = open("day7_problem2_test_data.txt", "r").readlines()

def get_child_bags(current_bag: str, rules: LuggageRules) -> int:
    child_bags = rules[current_bag].items()
    return sum(bag_count + (bag_count * get_child_bags(bag_name, rules)) 
                                            for bag_name,bag_count in child_bags)

def total_bags(rules: LuggageRules) -> int:
    return get_child_bags("shiny gold bag", rules)


def problem_2_test():
    count = total_bags(parse_luggage_rules(test_data2))
    assert count == 126

def problem_2():
    return total_bags(parse_luggage_rules(data))

problem_2_test()

print(f"Problem 2 answer: {problem_2()}")