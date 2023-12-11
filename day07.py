import dataclasses

from enum import IntEnum

_EXAMPLE_INPUT: str = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

_REAL_INPUT = """---snip---"""
_CARD_RANK = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


class HandType(IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


class Hand:
    hand_ids: str
    bid: int
    hand_type: HandType | None
    character_counts: list[tuple]

    def __init__(self, hand_ids: str, bid: int):
        self.hand_ids = hand_ids
        self.bid = bid
        self.hand_type = None

        self._compute_character_counts()
        self._compute_hand_type()

    def _compute_character_counts(self) -> None:
        character_counts = {}

        for char in self.hand_ids:
            # Use the get() method to get the current count or default to 0
            current_count = character_counts.get(char, 0)

            # Increment the count for the current character
            character_counts[char] = current_count + 1

        self.character_counts = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)

    def _compute_hand_type(self) -> None:
        if self.is_five_of_a_kind():
            self.hand_type = HandType.FIVE_OF_A_KIND
        elif self.is_four_of_a_kind():
            self.hand_type = HandType.FOUR_OF_A_KIND
        elif self.is_full_house():
            self.hand_type = HandType.FULL_HOUSE
        elif self.is_three_of_a_kind():
            self.hand_type = HandType.THREE_OF_A_KIND
        elif self.is_two_pair():
            self.hand_type = HandType.TWO_PAIR
        elif self.is_one_pair():
            self.hand_type = HandType.ONE_PAIR
        else:
            self.hand_type = HandType.HIGH_CARD

    def is_five_of_a_kind(self) -> bool:
        return len(self.character_counts) == 1

    def is_four_of_a_kind(self) -> bool:
        return self.character_counts[0][1] == 4

    def is_full_house(self) -> bool:
        return self.character_counts[0][1] == 3 and self.character_counts[1][1] == 2

    def is_three_of_a_kind(self) -> bool:
        if len(self.character_counts) != 3:
            return False

        return self.character_counts[0][1] == 3

    def is_two_pair(self) -> bool:
        if len(self.character_counts) != 3:
            return False

        return self.character_counts[0][1] == 2 and self.character_counts[1][1] == 2

    def is_one_pair(self) -> bool:
        return len(self.character_counts) == 4

    def is_high_card(self) -> bool:
        return len(self.character_counts) == 5


class HandPart2(Hand):
    def is_five_of_a_kind(self) -> bool:
        if len(self.character_counts) == 1:
            return True

        if len(self.character_counts) == 2 and 'J' in self.hand_ids:
            return True

        return False

    def is_four_of_a_kind(self) -> bool:
        """
                if 'J' in self.hand_ids:
            if len(self.character_counts) == 3:
                return True

        return super().is_four_of_a_kind()
        """

        if 'J' in self.hand_ids:
            if len(self.character_counts) == 3:
                if 'J' == self.character_counts[0][0] or 'J' == self.character_counts[1][0]:
                    return True
                if self.character_counts[0][1] == 3:
                    return True


        return super().is_four_of_a_kind()

    def is_full_house(self) -> bool:
        if 'J' in self.hand_ids:
            if len(self.character_counts) == 3 and (self.character_counts[0][1] == 3 or self.character_counts[0][1] == 2):
                return True

        return super().is_full_house()

    def is_three_of_a_kind(self) -> bool:
        if 'J' in self.hand_ids:
            if len(self.character_counts) == 4:
                return True

        return super().is_three_of_a_kind()


    def is_two_pair(self) -> bool:
        if 'J' in self.hand_ids:
            return len(self.character_counts) == 4

        return super().is_two_pair()

    def is_one_pair(self) -> bool:
        if 'J' in self.hand_ids:
            return True

        return super().is_one_pair()


def split_line_into_hand_ids_and_bid(line: str):
    hand_ids, bid = line.split(' ', 2)
    bid = int(bid)

    return hand_ids, bid


def get_hands(input_str: str) -> list[Hand]:
    lines = [line for line in input_str.splitlines() if len(line) > 0]

    hands = []
    for line in lines:
        hand_ids, bid = split_line_into_hand_ids_and_bid(line)
        hand = Hand(hand_ids=hand_ids, bid=bid)

        # print("Hand IDs: " + str(hand.hand_ids) + "\nhand_type: hand type: " + str(hand.hand_type.name) + "\n\n")
        hands.append(hand)

    return hands


def part1(input_str: str) -> int:
    hands = get_hands(input_str)
    hands_sorted_by_type = sorted(hands, key=lambda h: (
        int(h.hand_type),
        _CARD_RANK[h.hand_ids[0]],
        _CARD_RANK[h.hand_ids[1]],
        _CARD_RANK[h.hand_ids[2]],
        _CARD_RANK[h.hand_ids[3]],
        _CARD_RANK[h.hand_ids[4]],
    ))
    i = 1
    value = 0
    for hand in hands_sorted_by_type:
        value += (i * hand.bid)
        i += 1

    return value


def part2(input_str: str) -> int:
    lines = [line for line in input_str.splitlines() if len(line) > 0]
    hands = []
    for line in lines:
        hand_ids, bid = split_line_into_hand_ids_and_bid(line)
        hand = HandPart2(hand_ids=hand_ids, bid=bid)

        #print("Hand IDs: " + str(hand.hand_ids) + "\nhand_type: hand type: " + str(hand.hand_type.name) + "\n\n")
        hands.append(hand)

    # make J the lowest value when breaking ties
    _CARD_RANK['J'] = 1

    hands_sorted_by_type = sorted(hands, key=lambda h: (
        int(h.hand_type),
        _CARD_RANK[h.hand_ids[0]],
        _CARD_RANK[h.hand_ids[1]],
        _CARD_RANK[h.hand_ids[2]],
        _CARD_RANK[h.hand_ids[3]],
        _CARD_RANK[h.hand_ids[4]],
    ))
    i = 1
    value = 0
    for hand in hands_sorted_by_type:
        #print("Hand IDs: " + str(hand.hand_ids) + "\nhand_type: hand type: " + str(hand.hand_type.name) + "\n\n")
        value += (i * hand.bid)
        i += 1

    return value


print('part 1 answer: ' + str(part1(_REAL_INPUT)))
print('part 2 answer: ' + str(part2(_REAL_INPUT)))
#print('part 2 answer: ' + str(part2("62387 9")))
if __name__ == ' __main__':
    print('zzz')
    print('part 1 answer: ' + str(part1(_REAL_INPUT)))
