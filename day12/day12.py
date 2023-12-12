import dataclasses
from enum import StrEnum

import input


class GearState(StrEnum):
    Operational = '.'
    Damaged = '#'
    Unknown = '?'


class RowGears:
    pattern_requirements: list[int]
    gears: dict[str, GearState]

    def __init__(self, pattern_requirements: list[int], gears: dict[str, GearState]|str):
        if isinstance(gears, str):
            gears = RowGears.gears_from_string(gears)
        self.pattern_requirements = pattern_requirements
        self.gears = gears

    @property
    def gears_as_string(self) -> str:
        return ''.join(self.gears.values())

    def first_index_of_type(self, gear_state: GearState, starting_from: int = 0) -> int:
        return self.gears_as_string.find(gear_state.value, starting_from)

    def find_all_unknown_state_indexes(self) -> list[int]:
        return [int(index) for index, gear_state in self.gears.items() if gear_state == GearState.Unknown]

    @staticmethod
    def gears_from_string(gears_str: str) -> dict[str, GearState]:
        return {i: GearState(g) for i, g in enumerate(gears_str)}

    @property
    def gear_passes_requirements(self) -> bool:
        parts = [s for s in self.gears_as_string.split(GearState.Operational) if GearState.Damaged in s]
        if len(parts) != len(self.pattern_requirements):
            return False

        for i, damaged_str in enumerate(parts):
            if len(damaged_str) != int(self.pattern_requirements[i]):
                return False

        return True



def parse_input(input_str: str) -> list[RowGears]:
    def _parse_line(s: str) -> RowGears:
        gears_str, patterns_str = s.split(' ')
        patterns = patterns_str.split(',')

        gears = RowGears.gears_from_string(gears_str)

        return RowGears(pattern_requirements=patterns, gears=gears)

    return [_parse_line(line) for line in input_str.splitlines() if len(line) > 0]
def generate_combinations(original_string, indices, current_index=0, current_string=None, combinations=None):
    """
    Thanks ChatGPT
    """
    # Initialize combinations list and current string on first call
    if combinations is None:
        combinations = []
    if current_string is None:
        current_string = list(original_string)

    # Base case: if the current index is equal to the length of indices, add the current string to combinations
    if current_index == len(indices):
        combinations.append(''.join(current_string))
        return

    # Recursive case: replace the character at the current index with '.' and '#' and recurse
    for replacement in [GearState.Operational, GearState.Damaged]:
        new_string = current_string.copy()
        new_string[indices[current_index]] = replacement
        generate_combinations(original_string, indices, current_index + 1, new_string, combinations)

    return combinations
def part1(input_str: str) -> int:
    rows = parse_input(input_str)

    total_combinations = 0

    for row in rows:
        indexes_to_change = row.find_all_unknown_state_indexes()

        current_string = row.gears_as_string
        combinations = generate_combinations(row.gears_as_string, indexes_to_change)

        successful_patterns = []

        matches_for_row = 0
        for gear_str in combinations:
            combination_row_gears = RowGears(gears=gear_str, pattern_requirements=row.pattern_requirements)
            if combination_row_gears.gear_passes_requirements:
                print("Yay a match!")
                print(combination_row_gears.gears_as_string)
                total_combinations += 1
                matches_for_row += 1


        print('this row [' + row.gears_as_string + '] has ' + str(matches_for_row) + ' matches')
    print(rows)
    return total_combinations


if __name__ == '__main__':
    input_str = input.REAL_INPUT
    print("part 1: " + str(part1(input_str)))
