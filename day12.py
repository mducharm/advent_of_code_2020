from typing import List, Tuple
from enum import Enum
import math


test_data = open("day12_test_data.txt", "r").readlines()
data = open("day12_data.txt", "r").readlines()

# Problem 1

class Direction(Enum):
    East = "E"
    North = "N"
    West = "W"
    South = "S"

    Forward = "F"
    Right = "R"
    Left = "L"

DirectionDegrees = {
    "W": 0,
    "N": 90,
    "E": 180,
    "S": 270,
}

def direction_to_degrees(direction: Direction) -> int:
    return DirectionDegrees[direction.value]

def calculate_increment(direction: Direction, amount: int) -> Tuple[int, int]:
    if direction == Direction.East:
        return (amount, 0)
    if direction == Direction.North:
        return (0, amount)
    if direction == Direction.West:
        return (-amount, 0)
    if direction == Direction.South:
        return (0, -amount)

    return (0, 0)

def degrees_to_direction(degrees: int) -> Direction:

    degrees_to_directions = dict([(int(value), key) for key,value in DirectionDegrees.items()])

    degrees %= 360

    if degrees < 0:
        degrees += 360

    return Direction(degrees_to_directions[degrees])

Movements = List[Tuple[Direction, int]]

def next_coordinates(coord: Tuple[int, int], movements: Movements, previous_direction: Direction) -> Tuple[int, int]:

    if movements:
        next_direction, amount = movements[0] 

        # Only update direction if one of these conditions met. Use the new direction when calculating increment as well.
        if next_direction == Direction.Forward:
            next_direction = previous_direction

        if next_direction == Direction.Right:
            previous_degrees = direction_to_degrees(previous_direction)
            previous_degrees += amount
            previous_direction = next_direction = degrees_to_direction(previous_degrees)
            amount = 0

        if next_direction == Direction.Left:
            previous_degrees = direction_to_degrees(previous_direction)
            previous_degrees -= amount
            previous_direction = next_direction = degrees_to_direction(previous_degrees)
            amount = 0

        dx, dy = calculate_increment(next_direction, amount)

        x, y = coord

        x += dx
        y += dy

        remaining_movements = movements[1:]
        return next_coordinates((x, y), remaining_movements, previous_direction)

    return coord

def parse_data_into_movements(data: List[str]) -> Movements:
    return [(Direction(s[0]), int(s[1:])) for s in data]

def get_manhatten_distance(data: List[str], start_coords: Tuple[int, int], starting_direction: Direction) -> int:

    movements = parse_data_into_movements(data)

    x, y = next_coordinates(start_coords, movements, starting_direction)

    return abs(x) + abs(y)


def problem_1_test():
    assert get_manhatten_distance(test_data, (0, 0), Direction.East) == 25

def problem_1():
    return get_manhatten_distance(data, (0, 0), Direction.East)

problem_1_test()

print(f"Problem 1: {problem_1()}")

# Problem 2

Coordinates = Tuple[int, int]

def update_ship_coords(ship_coords: Coordinates, waypoint: Coordinates, amount: int) -> Coordinates:
    x, y = ship_coords
    dx, dy = waypoint
    return (x + dx * amount, y + dy * amount)

def update_waypoint(ship_coords: Coordinates, waypoint: Coordinates, direction: Direction, amount: int) -> Coordinates:

    x, y = waypoint

    if direction == direction.North:
        return (x, y + amount)
    if direction == direction.South:
        return (x, y - amount)
    if direction == direction.East:
        return (x + amount, y)
    if direction == direction.West:
        return (x - amount, y)
    if direction == direction.Right:
        for _ in range(0, amount, 90):
            x, y = y, -x
        return (x, y)
    if direction == direction.Left:
        for _ in range(0, amount, 90):
            x, y = -y, x
        return (x, y)

    return waypoint

def get_distance_with_waypoint(data: List[str], start_coords: Coordinates, starting_direction: Direction) -> int:

    movements = parse_data_into_movements(data)

    ship_coords = start_coords
    waypoint: Coordinates = (10, 1)

    for (direction, amount) in movements:

        if direction == Direction.Forward:
            ship_coords = update_ship_coords(ship_coords, waypoint, amount)
        else:
            waypoint = update_waypoint(ship_coords, waypoint, direction, amount) 

    x, y = ship_coords
 
    return abs(x) + abs(y)


def problem_2_test():
    assert get_distance_with_waypoint(test_data, (0, 0), Direction.East) == 286

def problem_2():
    return get_distance_with_waypoint(data, (0, 0), Direction.East)

problem_2_test()

print(f"Problem 2: {problem_2()}")