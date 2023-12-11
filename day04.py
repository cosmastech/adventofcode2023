_EXAMPLE_INPUT = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

_INPUT = """---snip---"""


def get_number_from_string(input_str: str) -> list[int]:
    return [int(s.strip(' ')) for s in input_str.split(' ') if len(s) > 0]


def get_game_number(input_str: str) -> int:
    input_str = input_str.replace('Card', '')
    return int(input_str.strip(' '))


def process_line(input_str: str) -> tuple[int, list[int]]:
    game_number_str, numbers_str = input_str.split(':', 2)

    card_number = get_game_number(game_number_str)

    winning_numbers_str, card_numbers_str = numbers_str.split('|')

    winning_numbers = get_number_from_string(winning_numbers_str)
    card_numbers = get_number_from_string(card_numbers_str)

    matches = [c for c in card_numbers if c in winning_numbers]

    return card_number, matches


def accumulate_cards(winners_per_card: dict):
    card_2 = {}
    for card_num, win in winners_per_card.items():
        card_2[card_num] = 1

    for card_num, winner_count in winners_per_card.items():
        for game_number in range(card_num+1, card_num + winner_count + 1):
            card_2[game_number] += 1*card_2[card_num]

    score = sum(card_2.values())
    print('score is: ' + str(score))


def main(input_str: str) -> None:
    card_count = {1: 1}

    winners_per_card = {}

    lines = [l for l in input_str.splitlines() if len(l) > 0]

    score = 0
    for line in lines:
        card_number, matches = process_line(line)

        match_count = len(matches)
        winners_per_card[card_number] = match_count

        if match_count == 0:
            continue

        score += 2 ** (match_count - 1)

    print('part 1: ' + str(score))
    accumulate_cards(winners_per_card)

if __name__ == '__main__':
    main(_INPUT)
