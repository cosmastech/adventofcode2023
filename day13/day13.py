from __future__ import annotations
from input import EXAMPLE_INPUT, REAL_INPUT



class GameBoard:
    board: list[str]
    width: int
    height: int

    def __init__(self, board: list[str]):
        self.board = board
        self.width = len(self.board[0])
        self.height = len(self.board)

    def search_for_reflection(self, left_starting_column: int = 0):
        for row_index in range(0, self.height):
            row: str = self.board[row_index]
            max_right_size: int = self.width - (left_starting_column + 1)
            max_left_size: int = left_starting_column
            chars_to_consider: int = min(max_left_size, max_right_size)

            left_side: str = row[left_starting_column - chars_to_consider + 1:left_starting_column + 1]
            right_side: str = row[left_starting_column + 1:left_starting_column + chars_to_consider + 1]

            left_side = ''.join(reversed(left_side))

            if left_side != right_side:
                return False

        return True

    def new_inverted_game_board(self) -> GameBoard:
        inverted: list[str] = [''.join(s) for s in zip(*self.board)]

        return GameBoard(inverted)

def parse_input_into_games(input_str: str) -> list[GameBoard]:
    board_strings = input_str.split("\n\n")

    games = [GameBoard(board_string.splitlines()) for board_string in board_strings]

    return games


def part1(input_str: str) -> int:
    games = parse_input_into_games(input_str)
    print(games)
    output = 0
    for game in games:
        column_start = 1
        found = False
        while column_start < (game.width-1):
            if game.search_for_reflection(column_start):
                print(f'{column_start} is a match')
                output += (column_start + 1)
                column_start+=1
                found = True
            column_start+=1

        inverted_game: GameBoard = game.new_inverted_game_board()
        column_start = 1
        if found:
            continue
        while column_start < (inverted_game.width - 1):
            if inverted_game.search_for_reflection(column_start):
                print(f'{column_start} is a match')
                output += (100 * (column_start + 1))
                column_start+=1
            column_start+=1

    return output


def part2(input_str: str) -> int:
    return 0


if __name__ == '__main__':
    input_str = REAL_INPUT
    print(f'Part 1: {part1(input_str)}')
    print(f'Part 2: {part2(input_str)}')
