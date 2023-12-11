import dataclasses
from enum import StrEnum, Enum, IntEnum

_EXAMPLE_INPUT_1="""
.....
.S-7.
.|.|.
.L-J.
....."""
_EXAMPLE_INPUT_2 = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

_REAL_INPUT="""---snip---"""
class Direction(IntEnum):
    North = 1
    East = 2
    South = 3
    West = 4

    def coming_from(self):
        if self.value == Direction.North:
            return Direction.South
        elif self.value == Direction.South:
            return Direction.North
        elif self.value == Direction.East:
            return Direction.West
        elif self.value == Direction.West:
            return Direction.East

    def next_coordinate(self) -> tuple:
        match(self.value):
            case Direction.North:
                return 0, -1
            case Direction.South:
                return 0, 1
            case Direction.East:
                return 1, 0
            case Direction.West:
                return -1, 0

class HowDidWeGetHere(Exception):
    pass

class Pipe(StrEnum):
    Vertical = '|'
    Horizontal = '-'
    NorthEast = 'L'
    NorthWest = 'J'
    SouthWest = '7'
    SouthEast = 'F'
    Ground = '.'
    Start = 'S'

    def possible_directions(self) -> tuple[Direction, Direction]:
        if self.value == Pipe.Vertical:
            return Direction.North, Direction.South
        elif self.value == Pipe.Horizontal:
            return Direction.East, Direction.West
        elif self.value == Pipe.NorthEast:
            return Direction.North, Direction.East
        elif self.value == Pipe.NorthWest:
            return Direction.North, Direction.West
        elif self.value == Pipe.SouthWest:
            return Direction.South, Direction.West
        elif self.value == Pipe.SouthEast:
            return Direction.South, Direction.East
        else:
            raise HowDidWeGetHere

    def next_direction(self, coming_from: Direction) -> Direction:
        choice1, choice2 = self.possible_directions()
        return choice1 if choice2 == coming_from else choice2


@dataclasses.dataclass
class Graph:
    starting_location: dict
    graph: list[list[Direction]]

@dataclasses.dataclass
class GraphWalker:
    current_location: tuple
    graph: Graph
    steps_from_start: int = 0

    def move_in_direction(self, d: Direction):
        possible_x, possible_y = d.next_coordinate()
        self.current_location = (self.current_location[0] + possible_x, self.current_location[1] + possible_y)
        #print('visited node: ')
        #print(self.current_location)
        self.steps_from_start += 1

    @property
    def current_pipe(self) -> Pipe:
        return self.graph.graph[self.current_location]


def convert_to_graph(input_str: str) -> Graph:

    output = {}

    lines = [l for l in input_str.splitlines() if len(l) > 0]

    for y, line in enumerate(lines):
        row = []
        for x, char in enumerate(line):
            pipe = Pipe(char)
            if pipe == Pipe.Start:
                starting_location = (x, y)
            output[(x, y)] = pipe

    return Graph(starting_location=starting_location, graph=output)


def part1(input_str: str) -> int:
    graph = convert_to_graph(input_str)

    walker = GraphWalker(graph.starting_location, graph)

    starting_x, starting_y = graph.starting_location
    starting_direction = None
    # Doesn't look like there are cases where S is in the corner
    if graph.graph[(starting_x + 1, starting_y)] in (Pipe.Horizontal, Pipe.NorthWest, Pipe.SouthWest):
        starting_direction = Direction.East
    elif graph.graph[(starting_x - 1, starting_y)] in (Pipe.Horizontal, Pipe.SouthEast, Pipe.NorthEast):
        starting_direction = Direction.West
    elif graph.graph[(starting_x, starting_y - 1)] in (Pipe.Vertical, Pipe.SouthEast, Pipe.SouthWest):
        starting_direction= Direction.North
    elif graph.graph[(starting_x, starting_y + 1)] in (Pipe.Vertical, Pipe.NorthEast, Pipe.NorthWest):
        starting_direction = Direction.South

    next_direction = starting_direction
    while True:
        walker.move_in_direction(next_direction)

        if walker.current_pipe == Pipe.Start:
            # we found the end
            break
        next_direction = walker.current_pipe.next_direction(next_direction.coming_from())

    return walker.steps_from_start // 2

def part2(input_str: str) -> int:
    pass

if __name__ == '__main__':
    input_str = _REAL_INPUT
    print('part 1: ' + str(part1(input_str)))
    print('part 2: ' + str(part2(input_str)))
