from input import REAL_INPUT, EXAMPLE_INPUT

def parse_input_str(input_str: str) -> list[str]:
    return input_str.split(',')

def parse_chunk(chunk_str: str) -> int:
    value: int = 0
    for char in chunk_str:
        value += ord(char)
        value *= 17
        value %= 256
    return value
def part1(input_str: str) -> int:
    output: int = 0

    chunks = parse_input_str(input_str)
    for chunk in chunks:
        output += parse_chunk(chunk)

    return output



if __name__ == '__main__':
    input_str = REAL_INPUT
    print("Part 1: " + str(part1(input_str)))
