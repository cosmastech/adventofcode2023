import dataclasses
import itertools

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
    # pairs_of_galaxy_indices = [(0, 1)]
    for pair in pairs_of_galaxy_indices:
        computed_shortest_distances.append(dist := shortest_distance(universe.grid[pair[0]], universe.grid[pair[1]]))
        print("locations: ")
        print(universe.grid[pair[0]], universe.grid[pair[1]])
        print(pair[0], pair[1], dist)
        # break
    return sum(computed_shortest_distances)


def expand_universe_part_2(s: str) -> list[int]:
    lines = split_lines(s)
    expanded = []
    for idx, line in enumerate(lines):
        if '#' not in line:
            expanded.append(idx)

    return expanded


def expand_universe(s: str) -> tuple[list[int], str]:
    o = []
    lines = split_lines(s)
    line_width = len(lines[0])
    expanded = []
    for idx, line in enumerate(lines):
        o.append(line)
        if '#' not in line:
            # need to expand
            o.append(' ' * line_width)
    return "\n".join(o)


def invert_str(input_str: str) -> str:
    lines = split_lines(input_str)
    columns = [''.join(column) for column in zip(*lines)]

    return "\n".join(columns)


def part2(input_str: str, multiplier: int = 1_000_000):
    universe = Universe(input_str)

    galaxy_indices = universe.grid.keys()

    pairs_of_galaxy_indices = list(itertools.combinations(galaxy_indices, 2))

    expanded_y_indexes = expand_universe_part_2(input_str)
    expanded_x_indexes = expand_universe_part_2(invert_str(input_str))

    def shortest_distance_part_2(galaxy1: Galaxy, galaxy2: Galaxy) -> int:
        x_values = [galaxy1.x, galaxy2.x]
        min_x = min(x_values)
        max_x = max(x_values)

        y_values = [galaxy1.y, galaxy2.y]
        min_y = min(y_values)
        max_y = max(y_values)

        times_multiplied = 0

        x_matches = [x for x in range(min_x, max_x) if x in expanded_x_indexes]
        y_matches = [y for y in range(min_y, max_y) if y in expanded_y_indexes]

        times_multiplied += len(x_matches)
        times_multiplied += len(y_matches)

        return abs(galaxy1.x - galaxy2.x) + abs(galaxy1.y - galaxy2.y) + (times_multiplied * (multiplier - 1))

    computed_shortest_distances = []
    for pair in pairs_of_galaxy_indices:
        computed_shortest_distances.append(
            dist := shortest_distance_part_2(universe.grid[pair[0]], universe.grid[pair[1]]))
        print("locations: ")
        print(universe.grid[pair[0]], universe.grid[pair[1]])
        print(pair[0], pair[1], dist)
        # break
    return sum(computed_shortest_distances)


if __name__ == '__main__':
    input_str = inputs.EXAMPLE_INPUT

    input_str = expand_universe(input_str)
    input_str = invert_str(input_str)

    input_str = expand_universe(input_str)
    input_str = invert_str(input_str)

    print(input_str)

    print("Part 1: " + str(part1(input_str)))

    input_str = inputs.REAL_INPUT
    print("Part 2: " + str(part2(input_str, 1_000_000)))
