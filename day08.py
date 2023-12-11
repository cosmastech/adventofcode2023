class Day8Input:
    t_indices: list[int]
    nodes: dict

    def __init__(self, top_line: str, map_str: str):
        self.t_indices = [
            int(v)
            for v in top_line.replace('L', '0').replace('R', '1')
            if v.isdigit()
        ]

        self.nodes = {}

        lines = [l for l in map_str.splitlines() if len(l) > 0]

        for line in lines:
            key, tuple_string = line.split(' = ')
            tuple_string: str
            v1, v2 = tuple_string.strip('()').split(', ')

            self.nodes[key] = (v1, v2)


def part1(input_object: Day8Input) -> int:
    print(input_object.nodes)
    print(input_object.t_indices)

    starting_node = 'AAA'
    ending_node = 'ZZZ'

    found = False
    curr_node = starting_node
    step_index = 0
    steps = 0
    while not found:
        if curr_node == ending_node:
            found = True
            continue
        curr_node = input_object.nodes[curr_node][input_object.t_indices[steps % len(input_object.t_indices)]]

        print('current node:' + curr_node)
        steps += 1

    return steps


if __name__ == '__main__':
    example_input = Day8Input("LLR", """AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""")
    real_input = Day8Input(
        "---snip---",
        """---snip---"""
    )
    print(f'Part 1: {part1(real_input)}')
