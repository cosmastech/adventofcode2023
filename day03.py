import pprint

_EXAMPLE_SCHEMATIC = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

_REAL_SCHEMATIC = """---snip---"""

_SPECIAL_CHARS = set()

CHAR_LOCATIONS = {}
NUMBER_LOCATIONS = {}
PART_2_NUMBER_LOCATIONS = {}


def parse_line(line: str, line_number: int):
    find_special_characters_in_line(line, line_number)
    for c in _SPECIAL_CHARS:
        line = line.replace(c, '.')

    curr_number_string = ''
    for i, c in enumerate(line):
        if c.isdigit():
            curr_number_string += c
            continue

        if len(curr_number_string) > 0:
            # we have a numeric string now
            starting_location = i - len(curr_number_string)
            NUMBER_LOCATIONS[(starting_location, line_number)] = (int(curr_number_string), len(curr_number_string))
            for x in range(starting_location, i):
                PART_2_NUMBER_LOCATIONS[(x, line_number)] = (
                int(curr_number_string), starting_location, starting_location + len(curr_number_string))
            curr_number_string = ''
    if len(curr_number_string) > 0:
        # we have a numeric string now
        starting_location = i - len(curr_number_string)
        NUMBER_LOCATIONS[(starting_location, line_number)] = (int(curr_number_string), len(curr_number_string))
        for x in range(starting_location, i):
            PART_2_NUMBER_LOCATIONS[(x, line_number)] = (
            int(curr_number_string), starting_location, starting_location + len(curr_number_string))


def find_special_characters_in_line(line: str, line_number: int):
    for special_character in _SPECIAL_CHARS:
        all_instances = [index for index, char in enumerate(line) if char == special_character]

        for i in all_instances:
            CHAR_LOCATIONS[(i, line_number)] = special_character


def _find_special_chars(input_str: str) -> None:
    for char in input_str:
        if not (char.isdigit() or char == '.' or char == '\n'):
            _SPECIAL_CHARS.add(char)


def find_numbers_adjacent_to_special_chars() -> list[int]:
    toReturn = []
    for number_location_tuple, number_details in NUMBER_LOCATIONS.items():
        found = False
        starting_x, y = number_location_tuple
        target_number = number_details[0]
        ending_x = starting_x + number_details[1]

        x_range = range(starting_x - 1, ending_x + 1)
        y_range = range(y - 1, y + 2)

        if target_number == 661:
            something_special = True
        for lookup_x in x_range:
            if found:
                break
            for lookup_y in y_range:
                if (lookup_x, lookup_y) in CHAR_LOCATIONS:
                    toReturn.append(target_number)
                    found = True
                    break

    return toReturn


def part1(input_str: str):
    _find_special_chars(input_str)
    lines = [l for l in input_str.splitlines() if len(l) > 0]

    for i, line in enumerate(lines):
        parse_line(line, i)

    pprint.pprint(CHAR_LOCATIONS)

    print(sum(find_numbers_adjacent_to_special_chars()))


def part2(input_str: str):
    _find_special_chars(input_str)

    lines = [l for l in input_str.splitlines() if len(l) > 0]

    for i, line in enumerate(lines):
        parse_line(line, i)

    gear_locations = [tup for tup, char in CHAR_LOCATIONS.items() if char == '*']

    toReturn = []
    for gear_x, gear_y in gear_locations:
        pair = []
        y_range = [gear_y - 1, gear_y, gear_y + 1]

        for y in y_range:
            x = gear_x - 1
            while x <= gear_x + 1:
                lookup_coordinate = (x, y)
                if lookup_coordinate in PART_2_NUMBER_LOCATIONS:
                    target_value, start_x, end_x = PART_2_NUMBER_LOCATIONS[lookup_coordinate]
                    pair.append(target_value)
                    x = end_x + 1
                else:
                    x += 1

        if len(pair) == 2:
            toReturn.append(pair[0] * pair[1])

    pprint.pprint(toReturn)
    print(sum(toReturn))


if __name__ == '__main__':
    part2(_REAL_SCHEMATIC)
