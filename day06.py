_EXAMPLE_INPUT = [(7, 9), (15, 40), (30, 200)]
_EXAMPLE_INPUT2 = [(71530, 940200)]
"""Real input:
Time:        49     87     78     95
Distance:   356   1378   1502   1882"""
_REAL_INPUT = [#---snip---
]

_REAL_INPUT2 = [(
    #snip
)]


def part1(list_of_tuples: list):
    final_answer = 1
    for time, max_distance in list_of_tuples:
        ways_to_win = []
        for holding_time in range(1, time):
            racing_time = time - holding_time

            rate = holding_time
            distance = rate * racing_time

            if distance > max_distance:
                ways_to_win.append(holding_time)
        if (l := len(ways_to_win)) > 0:
            final_answer *= l

    print('final answer: ' + str(final_answer))


if __name__ == '__main__':
    part1(_REAL_INPUT2)
