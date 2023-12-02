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

_REAL_INPUT = """Game 1: 4 blue, 16 green, 2 red; 5 red, 11 blue, 16 green; 9 green, 11 blue; 10 blue, 6 green, 4 red
Game 2: 15 green, 20 red, 8 blue; 12 green, 7 red; 10 green, 2 blue, 15 red; 13 blue, 15 red
Game 3: 8 red, 2 blue; 3 green, 10 blue, 10 red; 7 green, 4 blue, 7 red; 8 red, 6 green, 13 blue; 4 green, 3 blue, 10 red; 7 blue, 7 green, 5 red
Game 4: 13 green, 14 blue, 9 red; 6 green, 14 red, 18 blue; 9 red, 11 green, 3 blue; 11 green, 10 red, 14 blue; 17 blue, 3 red, 4 green; 17 blue, 1 red, 9 green
Game 5: 2 green, 1 red; 8 blue, 2 green, 6 red; 5 blue, 9 red, 2 green; 3 green, 8 red, 6 blue; 6 blue, 5 red
Game 6: 3 green, 7 blue, 5 red; 3 green, 6 red; 11 blue, 6 red, 1 green
Game 7: 8 red, 4 green, 11 blue; 12 blue, 1 green, 5 red; 6 red, 1 green, 5 blue; 12 blue, 2 green, 2 red; 4 blue, 4 green, 3 red; 9 blue, 4 green, 8 red
Game 8: 1 red, 4 green; 6 red, 1 green; 10 red; 1 blue, 2 green; 4 green, 3 red; 1 blue, 8 red
Game 9: 9 blue, 13 green, 1 red; 10 green, 4 blue, 4 red; 3 red, 4 blue, 14 green; 13 blue, 1 red, 12 green
Game 10: 2 blue, 16 red, 2 green; 1 green, 16 red, 6 blue; 9 red, 3 green; 1 green, 2 blue, 8 red; 8 red, 6 blue, 3 green
Game 11: 7 green, 11 red, 12 blue; 3 blue, 6 green, 6 red; 10 blue, 13 green; 1 red, 13 green, 9 blue; 2 blue, 2 red, 13 green; 2 red, 3 blue, 15 green
Game 12: 3 green, 2 red, 2 blue; 7 green, 5 blue; 1 blue, 1 red, 3 green
Game 13: 2 green, 2 red, 3 blue; 3 blue, 3 red, 3 green; 3 green, 2 red; 2 blue, 3 red, 3 green; 2 green, 3 red, 1 blue
Game 14: 4 green, 9 red; 11 green, 10 red, 12 blue; 6 red, 3 green, 12 blue; 5 green, 4 red, 4 blue; 18 blue, 7 red, 11 green; 16 blue, 4 red, 10 green
Game 15: 5 green, 2 red, 9 blue; 18 green, 6 red, 20 blue; 11 blue, 12 green, 11 red; 9 red, 17 blue, 16 green; 7 green, 1 red, 9 blue
Game 16: 9 blue, 11 green; 8 green, 2 blue; 1 red, 6 green, 4 blue
Game 17: 2 red, 2 green, 2 blue; 7 blue, 4 green, 3 red; 2 red, 8 blue, 1 green; 2 red, 6 blue, 2 green; 4 blue, 3 red; 4 green, 5 red, 6 blue
Game 18: 6 green, 7 red; 3 blue, 6 green, 1 red; 6 red, 3 blue, 5 green
Game 19: 6 red, 4 green, 5 blue; 2 red, 4 blue, 13 green; 1 green, 1 blue, 2 red; 4 green
Game 20: 7 red, 17 blue, 6 green; 3 blue, 6 green, 8 red; 7 blue, 6 red, 1 green; 3 green; 8 red, 7 green, 14 blue
Game 21: 5 red, 3 blue, 7 green; 1 blue, 2 red, 5 green; 2 blue, 8 green, 3 red; 3 blue, 8 red, 4 green; 5 red, 1 blue, 3 green
Game 22: 2 red, 6 green, 1 blue; 3 red, 3 green, 1 blue; 2 green, 7 red, 2 blue; 5 green, 1 red
Game 23: 2 red, 16 green, 1 blue; 1 red, 12 green, 3 blue; 12 green, 1 blue, 3 red
Game 24: 7 red, 1 blue, 12 green; 2 red, 19 green, 3 blue; 19 green, 1 blue, 12 red; 6 green, 16 red, 5 blue; 11 red, 4 blue, 12 green
Game 25: 2 blue, 3 red, 8 green; 4 blue, 2 red, 9 green; 2 red, 7 blue
Game 26: 17 red, 8 blue, 3 green; 3 green, 13 red, 4 blue; 20 red, 1 green, 6 blue; 7 blue, 2 red, 2 green; 20 red, 8 blue; 2 green, 16 red, 8 blue
Game 27: 3 blue, 17 green, 19 red; 16 green, 5 red, 6 blue; 17 green, 16 red, 4 blue
Game 28: 1 green, 7 red, 1 blue; 8 green, 12 red, 1 blue; 1 blue, 9 red, 1 green
Game 29: 3 green, 3 blue, 2 red; 3 green, 2 red, 1 blue; 3 green, 2 red, 3 blue; 3 blue, 3 red, 4 green
Game 30: 3 red, 8 blue, 3 green; 1 green, 1 red; 17 green, 17 blue; 19 green, 15 blue, 1 red; 1 green, 2 red, 16 blue
Game 31: 11 green, 11 blue, 14 red; 6 blue, 15 green, 2 red; 11 blue, 19 green, 2 red
Game 32: 9 red, 2 green; 7 green, 4 blue, 2 red; 6 red, 5 green, 1 blue; 4 red, 4 blue, 1 green; 8 red, 6 green
Game 33: 6 blue, 16 red, 9 green; 5 red, 7 blue, 13 green; 1 green, 9 blue, 1 red; 4 green, 9 blue, 17 red; 2 green, 10 red, 13 blue; 9 red, 1 blue, 14 green
Game 34: 2 red, 2 green, 4 blue; 3 blue, 2 green; 1 green, 1 red, 2 blue; 1 red, 3 blue, 3 green; 2 green, 8 blue, 2 red; 3 blue, 1 red
Game 35: 4 red, 14 blue, 2 green; 1 green, 15 blue, 1 red; 1 blue, 2 red, 1 green
Game 36: 4 blue, 1 red, 2 green; 2 green, 15 blue, 8 red; 7 blue, 1 red; 7 red, 1 green, 1 blue
Game 37: 2 blue, 1 green, 5 red; 2 blue, 2 green, 4 red; 2 blue, 5 red, 8 green; 3 green, 2 blue, 1 red; 1 red, 1 blue, 5 green; 2 blue, 1 red, 8 green
Game 38: 2 blue, 4 green, 11 red; 7 green, 6 red, 2 blue; 1 green, 3 red, 1 blue; 4 blue, 4 green, 4 red; 2 red, 5 blue, 2 green
Game 39: 7 green, 7 blue, 2 red; 11 blue, 4 green, 8 red; 10 red, 4 green, 1 blue; 8 green, 9 blue; 9 green, 4 red; 1 green, 8 blue
Game 40: 1 green, 13 blue; 6 blue, 7 red; 8 red; 1 green, 13 blue, 3 red; 1 green, 16 red, 13 blue; 14 blue, 14 red, 1 green
Game 41: 5 green, 2 blue, 10 red; 4 green, 2 blue, 5 red; 6 green, 9 red, 1 blue; 4 red, 1 blue; 1 red, 3 green, 2 blue; 3 red
Game 42: 17 green, 11 blue, 11 red; 5 blue, 11 green, 9 red; 10 blue, 13 red, 4 green; 8 green, 4 blue, 15 red
Game 43: 1 red, 3 blue; 1 green, 3 blue, 1 red; 2 blue, 1 green; 2 green, 1 blue; 1 red, 3 blue
Game 44: 7 green, 5 red, 1 blue; 6 green, 1 blue, 5 red; 2 blue, 6 green; 3 green, 2 red; 4 green; 6 red
Game 45: 16 red, 14 blue, 19 green; 1 red, 5 green, 6 blue; 16 blue, 2 green, 1 red; 15 green, 6 red, 16 blue
Game 46: 8 blue, 2 green; 4 red, 3 green, 6 blue; 1 green, 8 blue, 3 red; 3 green, 12 blue, 1 red
Game 47: 9 green, 3 blue; 1 green, 1 blue; 4 blue, 9 green, 6 red; 8 green, 4 blue, 6 red; 6 red, 12 green, 1 blue; 4 blue, 7 green
Game 48: 11 green, 4 blue, 1 red; 11 blue, 8 red, 9 green; 4 blue, 3 red, 7 green; 10 blue, 2 green, 9 red; 8 green, 2 blue, 2 red
Game 49: 8 green, 1 blue, 5 red; 1 green, 1 blue; 3 green, 4 red, 2 blue; 1 blue, 7 green, 1 red; 1 blue, 7 green, 3 red; 5 red, 5 green
Game 50: 2 green, 2 red, 4 blue; 8 blue, 2 green, 7 red; 4 blue, 5 red; 9 red, 4 blue; 5 blue, 9 red; 2 green, 8 red, 6 blue
Game 51: 6 green, 1 red, 2 blue; 2 red, 4 blue, 6 green; 9 blue, 4 green
Game 52: 7 green, 3 red, 12 blue; 8 blue, 9 red, 5 green; 2 blue, 10 green, 8 red; 12 red, 5 green, 3 blue; 8 red, 8 green, 12 blue; 2 green
Game 53: 2 green, 9 blue, 5 red; 6 red, 3 green; 5 red, 2 green
Game 54: 9 red, 13 blue; 1 green, 9 red, 16 blue; 12 red, 1 blue, 4 green
Game 55: 1 red, 2 blue, 3 green; 1 blue; 1 red, 5 blue, 3 green; 1 blue, 3 green; 5 blue
Game 56: 1 green, 4 red, 1 blue; 1 blue, 2 red, 13 green; 5 blue, 4 red; 13 green, 3 red, 3 blue
Game 57: 13 blue, 2 red, 7 green; 3 green, 4 red, 14 blue; 3 red, 3 green, 3 blue; 7 blue, 5 green, 1 red
Game 58: 6 red; 1 blue, 4 red, 2 green; 3 green, 1 blue; 7 green, 1 red; 6 red, 13 green, 1 blue; 3 red, 13 green, 1 blue
Game 59: 5 green, 10 red, 8 blue; 7 red, 3 green, 2 blue; 6 green, 3 red, 6 blue
Game 60: 2 green, 5 red, 15 blue; 2 green, 9 blue; 9 blue, 8 green, 3 red; 2 green, 6 red, 2 blue
Game 61: 8 blue, 3 green, 4 red; 1 red, 10 blue, 1 green; 4 red, 5 green, 3 blue; 3 red, 8 blue, 5 green
Game 62: 19 blue, 3 red, 14 green; 1 green, 7 blue, 1 red; 15 red, 20 blue, 6 green; 8 red, 4 green, 14 blue
Game 63: 13 red, 1 blue; 18 red, 4 green; 6 green, 9 red, 1 blue; 7 green, 1 blue, 9 red; 5 red, 1 blue, 4 green; 5 green, 1 blue, 17 red
Game 64: 2 green, 1 blue, 5 red; 2 red, 5 green; 6 red, 4 green
Game 65: 1 blue, 7 green, 1 red; 7 red, 1 green; 1 blue, 3 green, 3 red; 7 red, 3 green; 3 green, 7 red; 1 blue, 4 green
Game 66: 7 green, 6 blue, 8 red; 4 green, 9 red, 3 blue; 6 green, 4 blue; 5 blue, 2 green; 6 red, 4 green, 2 blue
Game 67: 10 blue, 17 green, 17 red; 11 red, 9 blue, 9 green; 9 blue, 19 red, 5 green; 5 red, 3 blue, 20 green; 11 red, 1 blue, 7 green
Game 68: 9 green, 4 red, 5 blue; 11 blue, 9 green, 2 red; 11 blue, 2 red, 6 green; 2 green, 6 red, 3 blue; 1 blue, 6 green, 4 red
Game 69: 3 red, 15 blue, 1 green; 4 red, 14 blue, 2 green; 4 red, 18 blue, 4 green
Game 70: 3 red, 8 green; 2 red, 6 green; 4 red, 2 blue, 2 green; 8 red, 1 green, 2 blue; 6 red, 3 blue, 4 green; 13 green, 8 red
Game 71: 3 green, 17 red; 2 red, 3 green; 2 green, 8 red, 1 blue; 11 red, 4 blue; 3 green, 11 red, 3 blue
Game 72: 1 red, 17 blue, 8 green; 2 red, 11 blue, 16 green; 3 red, 16 blue, 1 green; 2 red, 3 green, 10 blue
Game 73: 1 blue, 10 green, 8 red; 19 green, 10 red, 5 blue; 3 green, 13 red, 8 blue; 12 green, 4 blue; 2 green, 10 blue, 12 red
Game 74: 17 blue, 7 red, 10 green; 16 blue, 5 red; 9 blue, 7 green, 2 red; 10 red, 4 green, 14 blue
Game 75: 10 green, 5 blue, 4 red; 7 red, 10 blue, 7 green; 7 blue, 9 green, 2 red
Game 76: 13 green, 16 red, 20 blue; 4 red, 14 blue, 5 green; 12 red, 1 blue, 8 green
Game 77: 4 red, 2 green; 8 blue, 3 green, 2 red; 5 blue, 7 green, 3 red
Game 78: 12 green, 8 red, 8 blue; 10 green, 9 red, 10 blue; 16 blue, 1 red, 17 green; 4 red, 15 green, 13 blue
Game 79: 4 green, 2 red; 15 red, 3 blue; 15 red, 5 green
Game 80: 4 blue, 1 green, 13 red; 13 red, 1 blue, 5 green; 5 blue, 9 red; 3 blue, 3 green; 1 red; 3 red, 7 green, 6 blue
Game 81: 10 red, 3 green, 4 blue; 2 red, 5 green, 16 blue; 3 green, 1 blue; 9 blue, 2 green, 12 red
Game 82: 1 green, 9 blue, 1 red; 10 blue, 1 red, 1 green; 1 green, 7 blue; 8 blue
Game 83: 1 blue, 5 red; 2 blue, 3 red; 1 green, 2 blue, 1 red; 2 red, 1 blue, 1 green; 1 green, 1 blue; 2 red, 1 green
Game 84: 5 red, 14 blue, 2 green; 6 blue, 5 red, 8 green; 12 green, 3 blue, 5 red; 2 red, 10 green; 9 green, 14 blue
Game 85: 2 blue, 2 red; 14 red, 6 green, 5 blue; 5 green, 4 blue, 6 red; 8 red, 5 blue, 6 green
Game 86: 1 blue, 10 red; 4 red; 9 blue, 18 red, 3 green; 1 green, 1 blue, 7 red; 3 green, 8 red, 9 blue; 14 red, 2 green, 4 blue
Game 87: 1 green, 11 red, 8 blue; 1 green, 11 red, 2 blue; 7 red, 4 blue; 6 blue, 1 red, 2 green; 13 blue, 2 green; 6 blue, 12 red, 3 green
Game 88: 2 blue, 4 red, 8 green; 4 blue, 7 red; 3 red, 10 green, 4 blue; 9 green, 3 blue, 5 red; 4 red, 6 blue, 3 green
Game 89: 6 red, 10 green; 15 green, 15 red, 10 blue; 15 red, 1 green, 4 blue; 13 red, 6 blue, 4 green
Game 90: 17 green, 2 red, 1 blue; 6 green; 1 blue, 1 green; 1 blue, 16 green, 3 red; 14 green, 1 red
Game 91: 3 blue, 8 green; 3 green, 7 red, 9 blue; 12 blue; 9 red, 7 blue, 4 green; 1 green, 7 red, 1 blue
Game 92: 11 blue, 9 red, 12 green; 1 blue, 14 red, 6 green; 9 green, 6 red, 6 blue
Game 93: 1 red, 2 blue; 3 blue, 6 green; 1 red, 4 green, 3 blue
Game 94: 3 green, 3 blue; 1 red, 3 blue, 9 green; 3 blue, 10 green, 3 red; 10 green, 6 blue, 2 red; 9 blue, 14 green, 2 red; 1 red, 4 blue, 1 green
Game 95: 7 blue, 10 green; 3 blue, 5 green, 2 red; 4 blue, 10 green, 12 red; 6 green, 2 red, 6 blue
Game 96: 2 blue, 18 green, 8 red; 13 green, 3 blue, 3 red; 3 blue, 15 red, 8 green; 13 green, 10 red, 2 blue
Game 97: 14 blue, 2 red; 15 blue, 1 green, 2 red; 3 red, 6 blue, 1 green; 1 green, 14 blue, 4 red
Game 98: 4 blue, 9 red; 10 red, 1 green, 11 blue; 7 blue, 1 red; 1 red, 6 blue, 1 green
Game 99: 7 red, 6 green, 2 blue; 8 red; 16 green, 7 red, 4 blue
Game 100: 1 red, 1 green, 9 blue; 6 blue, 4 green, 3 red; 4 red, 2 green; 3 green, 2 red, 11 blue; 6 green, 5 blue, 1 red"""


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
