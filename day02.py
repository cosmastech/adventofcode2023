import dataclasses

_TEST_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

_TEST_CONSTRAINTS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

_REAL_INPUT = """---snip--"""


@dataclasses.dataclass
class GameRound:
    game_id: int
    min_red: int = None
    max_red: int = 0
    min_blue: int = None
    max_blue: int = 0
    min_green: int = None
    max_green: int = 0
    total_marbles_shown_at_once: int = 0


def process_run_details(run_details: str) -> list[dict]:
    individual_shows = run_details.split(';')

    return [process_individual_show(x) for x in individual_shows]


def extract_marble_and_color(s: str):
    number_of_marbles = int("".join(c for c in s if not c.isalpha()))

    s = s.lower()

    if "blue" in s:
        color = "blue"
    elif "red" in s:
        color = "red"
    elif "green" in s:
        color = "green"

    return (number_of_marbles, color)


def process_individual_show(individual_show: str):
    marble_details = [x.strip() for x in individual_show.split(',')]

    list_of_number_color_tuples = [extract_marble_and_color(x) for x in marble_details]

    output = {}

    for t in list_of_number_color_tuples:
        output[t[1]] = t[0]

    return output


def process_line(line: str):
    game_str: str
    run_details: str

    game_str, run_details = line.split(':', maxsplit=2)

    game_id = int(game_str.lower().replace('game ', ''))

    run_data = process_run_details(run_details)

    print(game_id, run_data)

    g = GameRound(game_id=game_id)

    colors = ["blue", "red", "green"]
    for run_dict in run_data:
        marbles_shown_in_round = 0
        for color in colors:
            if color in run_dict:
                key_max = "max_" + color
                key_min = "min_" + color
                number_of_marbles = run_dict.get(color)

                max_attr = getattr(g, key_max)
                min_attr = getattr(g, key_min)
                marbles_shown_in_round += number_of_marbles
                if getattr(g, key_max) < number_of_marbles:
                    setattr(g, key_max, number_of_marbles)

                if min_attr is None or min_attr < number_of_marbles:
                    setattr(g, key_min, number_of_marbles)
        if marbles_shown_in_round > g.total_marbles_shown_at_once:
            g.total_marbles_shown_at_once = marbles_shown_in_round

    return g


def get_game_rounds(input_str: str) -> list[GameRound]:
    return [process_line(s) for s in input_str.splitlines() if len(s) > 0]


def main(input_str: str, constraints: dict) -> None:
    game_rounds: list[GameRound] = get_game_rounds(input_str)

    red_constraint = constraints.get('red')
    blue_constraint = constraints.get('blue')
    green_constraint = constraints.get('green')
    total_marble_count = red_constraint + blue_constraint + green_constraint

    possible_ids = []
    for game_round in game_rounds:
        if game_round.total_marbles_shown_at_once > total_marble_count:
            continue

        if game_round.max_red > red_constraint:
            continue

        if game_round.max_blue > blue_constraint:
            continue

        if game_round.max_green > green_constraint:
            continue

        possible_ids.append(game_round.game_id)

    print(sum(possible_ids))


def get_game_round_power(game_round: GameRound) -> int:
    red = game_round.min_red if game_round.min_red != 0 else 1
    blue = game_round.min_blue if game_round.min_blue != 0 else 1
    green = game_round.min_green if game_round.min_green != 0 else 1

    return red * blue * green


def part2(input_str: str) -> None:
    game_rounds = get_game_rounds(input_str)
    print(game_rounds)
    for g in game_rounds:
        print(g, get_game_round_power(g))
    o = [get_game_round_power(game_round) for game_round in get_game_rounds(input_str)]

    print(sum(o))


if __name__ == '__main__':
    # main(_REAL_INPUT, _TEST_CONSTRAINTS)
    part2(_REAL_INPUT)
