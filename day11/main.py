import dataclasses
import itertools
import sys

import inputs


@dataclasses.dataclass
class Galaxy:
    x: int
    y: int


class Universe:
    grid: dict[int, Galaxy]

    def __init__(self, s: str):
        self.grid = {}
        self._convert_list_str_to_grid(s)

    def _convert_list_str_to_grid(self, lines: str) -> None:
        lines = split_lines(lines)

        index = 0
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == '#':
                    galaxy = Galaxy(x=x, y=y)
                    self.grid[index] = galaxy
                    index += 1



def split_lines(s: str) -> list[str]:
    return [l for l in s.splitlines() if len(l) > 0]

def shortest_distance(galaxy1: Galaxy, galaxy2: Galaxy) -> int:
    return abs(galaxy1.x - galaxy2.x) + abs(galaxy1.y - galaxy2.y)

def part1(input_str: str) -> int:
    universe = Universe(input_str)

    galaxy_indices = universe.grid.keys()

    pairs_of_galaxy_indices = list(itertools.combinations(galaxy_indices, 2))

    computed_shortest_distances = []
    #pairs_of_galaxy_indices = [(0, 1)]
    for pair in pairs_of_galaxy_indices:
        computed_shortest_distances.append(dist := shortest_distance(universe.grid[pair[0]], universe.grid[pair[1]]))
        print("locations: ")
        print(universe.grid[pair[0]], universe.grid[pair[1]])
        print(pair[0], pair[1], dist)
        #break
    return sum(computed_shortest_distances)

def expand_universe(s: str) -> str:
    o = []
    lines = split_lines(s)
    line_width = len(lines[0])
    for line in lines:
        o.append(line)
        if '#' not in line:
            # need to expand
            o.append(' ' * line_width)
    return "\n".join(o)

def invert_str(input_str: str) -> str:
    lines = split_lines(input_str)
    columns = [''.join(column) for column in zip(*lines)]

    return "\n".join(columns)

if __name__ == '__main__':
    input_str: str = """...#.#...#"""
    input_str = inputs.REAL_INPUT

    input_str = expand_universe(input_str)
    #print(input_str)
    input_str = invert_str(input_str)

    input_str = expand_universe(input_str)
    input_str = invert_str(input_str)

    print(input_str)

    print("Part 1: " + str(part1(input_str)))
