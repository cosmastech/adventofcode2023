from math import gcd
from functools import reduce


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

    @property
    def nodes_ending_with_a(self) -> list[str]:
        return [k for k in self.nodes.keys() if k[-1] == 'A']


class Walker:
    input_obj: Day8Input

    def __init__(self, input_obj: Day8Input):
        self.input_obj = input_obj

    def get_next_node(self, starting_node: str, step: int = 0) -> str:
        counter = (step) % len(self.input_obj.t_indices)
        tuple_index = self.input_obj.t_indices[counter]

        return self.input_obj.nodes[starting_node][tuple_index]


real_input = Day8Input(
    "---snip---",
    """---snip---"""
)

_example_input_part_2 = Day8Input("LR", """11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""")


def is_ending_node(s: str) -> bool:
    return s[-1] == 'Z'


def lcm(a, b) -> int:
    return abs(a * b) // gcd(a, b)


def part2(input_obj: Day8Input, run_to: int = 200):
    walker = Walker(input_obj)

    ending_nodes = {}
    for node in input_obj.nodes_ending_with_a:
        if node not in ending_nodes:
            ending_nodes[node] = []

        current_node = node
        for step in range(0, run_to):
            current_node = walker.get_next_node(current_node, step)
            print(f'Step: {step} -- node: {current_node}')
            if (is_ending_node(current_node)):
                ending_nodes[node].append(step + 1)

    """
    I bring dishonor to my family to admit this, but I leveraged ChatGPT a bit. I started with a brute force approach
    but that just didn't work out (ran for hours and still climbing). So I decided to try to look at it mathematically:
    can we turn each starting node and get the resulting step count where it *could* terminate. But I thought that
    maybe I would need to look for cases where the results got stuck in loops. I asked ChatGPT to help me write a
    function for detecting cycles in graphs, but I don't think it was the right approach.
    
    Sullen, I decided to just map out all of the terminating values for some random range (I went with 999999 because I
    figured I could at least start somewhere and make sure my output even made sense). I then asked ChatGPT,
    "Does that appear to be a cycle in any of these?" and it gave me a really fucking passive aggressive answer acting
    like I don't know what a cycle is (it turns out I probably don't).
    
    It said, no, they're all arithmetic series. Each case just adds on by the starting value. [12, 24, 36, ...] A ha!
    
    So, we can just take the least common multiple for each starting index and that would tell us the first step-count
    where all of them intersect.
    
    I also asked ChatGPT how to compute the LCM in Python because I have a meeting starting shortly and all
    I would've been doing anyways was looking it up. 
    """

    steps = [steps[0] for steps in ending_nodes.values()]
    return reduce(lcm, steps)


if __name__ == '__main__':
    # print(part2(_example_input_part_2))
    # 99999 is just some random ass guess as to what might be too high
    print('LCM: ' + str(part2(real_input, 999999)))
