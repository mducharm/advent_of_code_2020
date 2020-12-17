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

class ConwayCubes():


    def __init__(self, data: List[str]) -> None:
        self.grid: Grid = self._get_initial_layer(data)

    def _get_initial_layer(self, data: List[str]) -> Grid:

        first_layer: List[List[State]] = [[State(state) for state in list(states.strip())] for states in data]

        grid: Grid = {}

        grid[0] = {
                idx: {
                    row_idx: state for row_idx, state in enumerate(row)
                }
                for idx, row in enumerate(first_layer)
            }

        return grid

    # def _cube_iter(self) -> Generator[Tuple[Coordinates, State], None, None]:
    def _cubes(self) -> List[Tuple[Coordinates, State]]:

        grid = self.grid.items()

        cubes = []

        for z_idx, xy_layer in grid:
            for y_idx, x_layer in xy_layer.items():
                for x_idx, state in x_layer.items():
                    cubes.append(((x_idx, y_idx, z_idx), state))

        return cubes

    def _get_neighbor_cubes(self, coords: Coordinates) -> List[Coordinates]:
        x, y, z = coords

        # possible_differences = [t for t in product([-1, 0, 1], repeat=3) if 0 in t and t != (0, 0, 0)]
        possible_differences = [t for t in product([-1, 0, 1], repeat=3) if t != (0, 0, 0)]

        neighbor_coordinates = [(x + dx, y + dy, z + dz) for dx, dy, dz in possible_differences]

        return neighbor_coordinates


    def _get_state(self, coords: Coordinates, grid: Grid) -> State:
        x, y, z = coords

        if z not in grid.keys():
            grid[z] = {}

        if y not in grid[z].keys():
            grid[z][y] = {}

        if x not in grid[z][y].keys():
            grid[z][y][x] = State.Inactive

        return grid[z][y][x]

    def _set_state(self, coords: Coordinates, new_state: State) -> None:
        x, y, z = coords

        if z not in self.grid.keys():
            self.grid[z] = {}

        if y not in self.grid[z].keys():
            self.grid[z][y] = {}

        if x not in self.grid[z][y].keys():
            self.grid[z][y][x] = State.Inactive

        self.grid[z][y][x] = new_state


    def _determine_next_state(self, coords: Coordinates, current_state: State, current_grid: Grid) -> State:

        # current_state = self._get_state(coords)

        neighbor_cubes = self._get_neighbor_cubes(coords)

        neighbor_states = [self._get_state(c, current_grid) for c in neighbor_cubes]

        num_of_active_neighbors = sum(x == State.Active for x in neighbor_states)

        if current_state == State.Active:
            if num_of_active_neighbors in (2, 3):
                return State.Active
            else:
                return State.Inactive
        else:
            if num_of_active_neighbors == 3:
                return State.Active
            else:
                return State.Inactive

        # if current_state == State.Active:
        #     if num_of_active_neighbors in (2, 3):
        #         self._set_state(coords, State.Active)
        #     else:
        #         self._set_state(coords, State.Inactive)
        # else:
        #     if num_of_active_neighbors == 3:
        #         self._set_state(coords, State.Active)
        #     else:
        #         self._set_state(coords, State.Inactive)

        return State.Inactive

    def run_boot_process(self, cycles: int) -> None:

        while cycles > 0:

            active_cubes = self.get_num_of_active_cubes()

            current_grid: Grid = self.grid.copy()

            for cube in self._cubes():

                coords, state = cube

                next_state = self._determine_next_state(coords, state, current_grid)

                self._set_state(coords, next_state)

            # for each cube - (x, y, z)
            # get cube's current state
            # get next state based on current
            # set next state

            cycles -= 1


    def get_num_of_active_cubes(self) -> int:
        return sum(state == State.Active for _, state in self._cubes())


def problem_1():
    cubes = ConwayCubes(data)
    cubes.run_boot_process(6)
    return cubes.get_num_of_active_cubes()

def problem_2():
    pass

if __name__ == '__main__':
    problem_1()
    problem_2()