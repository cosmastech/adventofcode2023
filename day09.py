def split_lines(input_str: str) -> list[str]:
    return [l for l in input_str.splitlines() if len(l) > 0]


def parse_line(line: str) -> list[int]:
    return [int(c) for c in line.split(' ') if len(c) > 0]


def compute_line_differences(numbers: list[int]) -> list[int]:
    starting_value = numbers[0]
    line_differences = []
    for curr_number in numbers[1:]:
        line_differences.append(curr_number - starting_value)
        starting_value = curr_number

    return line_differences


def get_line_differences_until_all_zeroes(number_sequence: list[int]) -> list[list[int]]:
    output = [number_sequence]

    while True:
        output.append(line_differences := compute_line_differences(number_sequence))

        if sum(line_differences) == 0:
            break

        number_sequence = line_differences

    return output

def get_new_final_value(number_sequence: list[int], to_make: int) -> int:
    last_digit = number_sequence[-1]

    return last_digit + to_make

def get_new_starting_value(number_sequence: list[int], to_make: int) -> int:
    first_digit = number_sequence[0]

    return first_digit-to_make
def part1(input_str: str) -> int:
    lines_str = split_lines(input_str)
    lines = [parse_line(line_str) for line_str in lines_str]

    sum = 0
    for number_sequence in lines:
        sequence_list = get_line_differences_until_all_zeroes(number_sequence)
        sequence_list.reverse()

        to_make = 0
        for inner_number_sequence in sequence_list:
            to_make = get_new_final_value(inner_number_sequence, to_make)
            inner_number_sequence.append(to_make)

        #print(inner_number_sequence)
        sum += sequence_list[-1][-1]

    return sum


def part2(input_str: str) -> int:
    lines_str = split_lines(input_str)
    lines = [parse_line(line_str) for line_str in lines_str]

    sum = 0
    for number_sequence in lines:
        sequence_list = get_line_differences_until_all_zeroes(number_sequence)
        sequence_list.reverse()

        to_make = 0
        for inner_number_sequence in sequence_list:
            to_make = get_new_starting_value(inner_number_sequence, to_make)
            inner_number_sequence.insert(0, to_make)

        #print(inner_number_sequence)
        sum += sequence_list[-1][0]

    return sum


_EXAMPLE_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

_REAL_INPUT="""---snip---"""

if __name__ == '__main__':
    #print('part 1: ' + str(part1(_REAL_INPUT)))
    print('part 2: ' + str(part2(_REAL_INPUT)))
