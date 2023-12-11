import json
import re

INPUT_DATA = """
---snip--- put your real input here
"""

EXAMPLE_INPUT = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

EXAMPLE_WITH_WORDS = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def main(input_data: str):
    output = [get_digits_2(i) for i in input_data.splitlines() if len(i) > 0]

    print(output)
    total = 0
    for line_count in output:
        total += int(line_count)

    return total


spelled_numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}

numbers_as_strings = {
    str(i): i for i in range(10)
}


def get_digits_2(input_str: str) -> int:
    o = {}
    for k, v in {**numbers_as_strings, **spelled_numbers}.items():
        first_occurrence = input_str.find(k)
        last_occurrence = input_str.rfind(k)
        if first_occurrence != -1:
            o[first_occurrence] = v
        if last_occurrence != -1:
            o[last_occurrence] = v

    return int(str(o[min(o)]) + str(o[max(o)]))


def get_digits(input: str) -> int:
    ints = [d for d in input if d in "1234567890"]

    print(ints)

    return int(str(ints[0]) + str(ints[-1]))


if __name__ == "__main__":
    print(main(INPUT_DATA))
