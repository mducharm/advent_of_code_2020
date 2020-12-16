from shared.helper import chunk_by_blank_lines
from typing import Dict, List, Set, Tuple
from shared.helper import get_input
from dataclasses import dataclass
import math
import re

data = get_input(__file__)


Rules = Dict[str, List[Set[int]]]

@dataclass
class TicketData():
    rules: Rules
    my_ticket: List[int]
    nearby_tickets: List[Set[int]]
    nearby_tickets_as_lists: List[List[int]]

def parse_ticket_data(data: List[str]) -> TicketData:
    ticket_data: List[List[str]] = chunk_by_blank_lines(data)

    rules, my_ticket, nearby_tickets = ticket_data[0], ticket_data[1], ticket_data[2]

    return TicketData(
        parse_rules(rules),
        [int(num) for num in my_ticket[1].split(",")],
        [{int(num) for num in ticket.split(",")} for ticket in nearby_tickets[1:]],
        [[int(num) for num in ticket.split(",")] for ticket in nearby_tickets[1:]]
    )


def parse_rules(data: List[str]) -> Rules:
        rule_pattern = r"^(?P<name>.+): (?P<first_range>[0-9]+-[0-9]+) or (?P<second_range>[0-9]+-[0-9]+)"
        rules = (
            (line.group("name"), line.group("first_range").split("-"), line.group("second_range").split("-"))
            for matches in data
            for line in re.finditer(rule_pattern, matches) 
        )

        return {
            name: [
                set(range(int(first_range[0]), int(first_range[1]) + 1)),
                set(range(int(second_range[0]), int(second_range[1]) + 1)),
            ]
            for name, first_range, second_range in rules
        }
        
def get_all_valid_numbers(ranges: List[Set[int]]) -> Set[int]:
    return set().union(*ranges)

def filter_out_invalid_tickets(data: TicketData) -> TicketData:

    valid_nums = get_all_valid_numbers([nums for rule in data.rules.values() for nums in rule])

    data.nearby_tickets = [ticket for ticket in data.nearby_tickets if ticket.issubset(valid_nums)]
    data.nearby_tickets_as_lists = [ticket for ticket in data.nearby_tickets_as_lists if set(ticket).issubset(valid_nums)]

    return data

def slice_tickets_into_columns(data:TicketData) -> List[List[int]]:
    ticket_columns: List[List[int]] = []

    for ticket_numbers in data.nearby_tickets_as_lists:
        for idx, num in enumerate(ticket_numbers):
            try: 
                ticket_columns[idx].append(num)
            except IndexError:
                ticket_columns.append([num])

    return ticket_columns

def get_ticket_scanning_error_rate(data: List[str]) -> int:

    ticket_data = parse_ticket_data(data)

    rules = ticket_data.rules
    nearby_tickets = ticket_data.nearby_tickets

    valid_nums = get_all_valid_numbers([nums for rule in rules.values() for nums in rule])

    invalid_tickets = (ticket for ticket in nearby_tickets if not ticket.issubset(valid_nums))

    invalid_nums = (num for ticket in invalid_tickets for num in ticket if num not in valid_nums)
    
    return sum(invalid_nums)

def get_rule_positions(data: List[str]) -> Tuple[Dict[str, int], TicketData]:
    ticket_data = parse_ticket_data(data)

    valid_tickets = filter_out_invalid_tickets(ticket_data)

    ticket_columns = slice_tickets_into_columns(valid_tickets)

    rule_positions: Dict[str, int] = {}
    remaining_rules: Set[str] = set(ticket_data.rules.keys())

    for key, rule_sets in ticket_data.rules.items():

        rule_nums: Set[int] = set().union(*rule_sets)

        for idx, column in enumerate(ticket_columns):
            if set(column).issubset(rule_nums) and idx not in rule_positions.values():
                rule_positions[key] = idx
                remaining_rules.remove(key)
                break

    # Check for duplicate positions
    assert len(rule_positions.values()) == len(set(rule_positions.values()))

    return rule_positions, ticket_data

def get_product_of_departure_fields(data: List[str]) -> int:
    rule_positions, ticket_data = get_rule_positions(data) 
    positions_of_departure_fields = [x for key, x in rule_positions.items() if "departure" in key]

    assert len(positions_of_departure_fields) == 6
    values = (x for idx, x in enumerate(ticket_data.my_ticket) if idx in positions_of_departure_fields)
    return math.prod(values)

def problem_1():
    return get_ticket_scanning_error_rate(data)

def problem_2():
    return get_product_of_departure_fields(data)

if __name__ == '__main__':
    # problem_1()
    # 576481 is too low...?
    problem_2()