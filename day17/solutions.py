from itertools import product
from typing import Dict, Generator, List, Tuple
from shared.helper import get_input
from enum import Enum

data = get_input(__file__)

class State(Enum):
    Active = "#"
    Inactive = "."

Grid = (
    Dict[int, 
        Dict[int, 
            Dict[int, State]
            ]
        ]
    )
    # To get a particular coordinate's state, do:
    # grid[z][y][x] = State

Coordinates = Tuple[int, int, int]

Cube = Tuple[Coordinates, State]


def get_next_iteration(initial_cubes: List[Cube]) -> List[Cube]:

    next_cubes = []

    cubes = []

    # Need to check the neighbors of all existing cells as well, 
    # since there cells not in the initial list that 
    for cube in initial_cubes:
        neighbor_cubes = get_neighbor_cubes(cube, cubes)
        for c in neighbor_cubes:
            cubes.append(c)

        cubes.append(cube)


    for cube in cubes:
        # Get neighbors
        neighbor_cubes = get_neighbor_cubes(cube, cubes)

        num_of_active_neighbors = sum(state == State.Active for _, state in neighbor_cubes)

        coords, state = cube

        # Determine next state:
        if num_of_active_neighbors == 3:
            next_cubes.append((coords, State.Active))
        elif num_of_active_neighbors == 2 and state == State.Active:
            next_cubes.append((coords, State.Active))
        else:
            next_cubes.append((coords, State.Inactive))

    return next_cubes


def get_initial_layer(data: List[str]) -> List[Cube]:
    return [
            ((x, y, 0), State(state))
            for y, column in enumerate(data)
            for x, state in enumerate(column.strip())
        ]


def get_neighbor_cubes(cube: Cube, all_cubes: List[Cube]) -> List[Cube]:

    coords, _ = cube
    x, y, z = coords

    possible_differences = (t for t in product([-1, 0, 1], repeat=3) if t != (0, 0, 0))

    neighbor_coordinates = ((x + dx, y + dy, z + dz) for dx, dy, dz in possible_differences)

    neighbor_cubes = []

    for coord in neighbor_coordinates:

        if (coord, State.Active) in all_cubes:
            neighbor_cubes.append((coord, State.Active))
        else:
            neighbor_cubes.append((coord, State.Inactive))

    return neighbor_cubes


def cycle_cubes(data: List[str], num: int) -> int:
    cubes = get_initial_layer(data)

    for _ in range(num):
        cubes = get_next_iteration(cubes)

    return sum(state == State.Active for _, state in cubes)

def problem_1():
    return cycle_cubes(data, 6)

def problem_2():
    pass

if __name__ == '__main__':
    problem_1()
    problem_2()