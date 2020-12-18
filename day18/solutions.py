from typing import Callable, Deque, List
from shared.helper import get_input
from collections import deque
 

data = get_input(__file__)

# Problem 1

def convert_to_RPN(exp: str) -> Deque[str]:
    output = deque()
    operator_stack = deque()

    while exp:
        next_char = exp[0]

        if next_char.isnumeric():
            output.append(next_char)
        elif next_char == "(":
            operator_stack.append(next_char)
        elif next_char == ")":

            while len(operator_stack) != 0 and operator_stack[-1] != "(":
                output.append(operator_stack.pop())
            if len(operator_stack) != 0 and operator_stack[-1] == "(":
                operator_stack.pop()
        elif next_char in ("+", "*"):
            while operator_stack and operator_stack[-1] != "(":
                output.append(operator_stack.pop())
            operator_stack.append(next_char)

        exp = exp[1:]

    while operator_stack:
        output.append(operator_stack.pop())

    return output

def process_math_problem(p: str, convert: Callable[[str], Deque[str]]) -> int:

    result = 0
    problem = p.replace(" ", "").strip()

    # exp_as_rpn = convert_to_RPN(problem)
    exp_as_rpn = convert(problem)

    stack = deque()

    for next_item in exp_as_rpn:

        if next_item.isnumeric():
            stack.append(next_item)

        elif next_item in ("+", "*"):
            first = int(stack.pop())
            second = int(stack.pop())

            result = first + second if next_item == "+" else first * second
            stack.append(str(result))

    return int(stack.pop())


def sum_all_problems(data: List[str], convert: Callable[[str], Deque[str]]) -> int:
    return sum(process_math_problem(p, convert) for p in data)

def problem_1():
    return sum_all_problems(data, convert_to_RPN)

# Problem 2

def precedence_level(op: str) -> int:
    return 1 if op == "+" else 0

def convert_to_RPN_with_precedence(exp: str) -> Deque[str]:
    output = deque()
    operator_stack = deque()

    while exp:
        next_char = exp[0]

        if next_char.isnumeric():
            output.append(next_char)
        elif next_char == "(":
            operator_stack.append(next_char)
        elif next_char == ")":
            while len(operator_stack) != 0 and operator_stack[-1] != "(":
                output.append(operator_stack.pop())
            if len(operator_stack) != 0 and operator_stack[-1] == "(":
                operator_stack.pop()
        elif next_char in ("+", "*"):
            while operator_stack and operator_stack[-1] != "(" and precedence_level(operator_stack[-1]) > precedence_level(next_char):
                output.append(operator_stack.pop())
            operator_stack.append(next_char)

        exp = exp[1:]

    while operator_stack:
        output.append(operator_stack.pop())

    return output

def problem_2():
    return sum_all_problems(data, convert_to_RPN_with_precedence)
    

if __name__ == '__main__':
    sum_all_problems(data, convert_to_RPN)
    sum_all_problems(data, convert_to_RPN_with_precedence)