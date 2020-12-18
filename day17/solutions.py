from itertools import product
import itertools
from typing import List, Set, Tuple
from shared.helper import get_input

data = get_input(__file__)

Coordinates = Tuple[int, int, int]

def get_next_iteration(active_cubes: Set[Coordinates]) -> Set[Coordinates]:

    next_cubes = set()

    for cube in active_cubes:
        neighbor_cubes = get_neighbor_cubes(cube)

        active_neighbors = neighbor_cubes.intersection(active_cubes)

        # Only add currently active cube to next list if it should be active.
        if len(active_neighbors) - 1 in (2, 3):
            next_cubes.add(cube)

        inactive_neighbors = neighbor_cubes - active_cubes

        for n in inactive_neighbors:
            neighbors_neighbors = get_neighbor_cubes(n)

            active_neighbors_neighbors = neighbors_neighbors.intersection(active_cubes)

            if len(active_neighbors_neighbors) == 2:
                next_cubes.add(n)

    return next_cubes


def get_initial_layer(data: List[str]) -> Set[Coordinates]:
    return {
            (x, y, 0) 
            for y, column in enumerate(data)
            for x, s in enumerate(column.strip())
            if s == "#"
        }

def get_neighbor_cubes(coord: Coordinates) -> Set[Coordinates]:

    x, y, z = coord

    possible_differences = (t for t in product([-1, 0, 1], repeat=3) if t != (0, 0, 0))

    neighbor_coordinates = {
        (x + dx, y + dy, z + dz) 
        for dx, dy, dz in possible_differences
        }

    return neighbor_coordinates


def cycle_cubes(data: List[str], num_of_cycles: int) -> int:

    coords = get_initial_layer(data)

    for _ in itertools.repeat(None, num_of_cycles):

        coords = get_next_iteration(coords)

    return len(coords)

def problem_1():
    return cycle_cubes(data, 6)

def problem_2():
    pass

if __name__ == '__main__':
    problem_1()
    problem_2()