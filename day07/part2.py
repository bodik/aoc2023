#!/usr/bin/env python3
"""
aoc2021 solution skeleton

A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
"""

import logging
from argparse import ArgumentParser
from pathlib import Path

from enum import IntEnum

class Card(IntEnum):
    _J = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    _T = 10
    _Q = 12
    _K = 13
    _A = 14


from collections import Counter

def identify_combinations(cards):  # gpt assisted
    values = cards
    value_count = Counter(values)
    
    if max(value_count.values()) == 5:
        return 7, "Five of a Kind"
    if max(value_count.values()) == 4:
        return 6, "Four of a Kind"
    elif sorted(value_count.values()) == [2, 3]:
        return 5, "Full House"
    elif max(value_count.values()) == 3:
        return 4, "Three of a Kind"
    elif sorted(value_count.values()) == [1, 2, 2]:
        return 3, "Two Pair"
    elif max(value_count.values()) == 2:
        return 2, "One Pair"
    else:
        return 1, "High Card"

    raise ValueError('unidentified hand')


class Hand:
    def __init__(self, cards, bid):
        self.cards = [Card[f'_{x}'] for x in cards]
        self.orig_strength, self.orig_name = identify_combinations(self.cards)
        self.bid = bid

        self.strength, self.name = self.orig_strength, self.orig_name

        def generate_variations(lst, indexes, current_index=0, variation=[], variations=[]):  # gpt assisted
            if current_index == len(indexes):
                variations.append(list(variation))
                return
        
            for value in Card:
                variation[indexes[current_index]] = value
                generate_variations(lst, indexes, current_index + 1, variation, variations)
        
            return variations

        jokers = [idx for idx, card in enumerate(self.cards) if card == Card['_J']]
        if jokers:
            variations = generate_variations(self.cards, jokers, 0, self.cards.copy(), [])
            max_strength = 0
            max_name = None
            for variation in variations:
                tmp_strength, tmp_name = identify_combinations(variation)
                if tmp_strength > max_strength:
                    max_strength = tmp_strength
                    max_name = tmp_name
            self.strength = max_strength
            self.name = max_name

    def __repr__(self):
        return f'<Hand {self.cards} n:{self.name} s:{self.strength} b:{self.bid}>'

    def __eq__(self, other):
        return (self.strength == other.strength) and (self.cards == other.cards)

    def __lt__(self, other):
        if self.strength < other.strength:
            return True
        if self.strength > other.strength:
            return False
        return self.cards < other.cards

    def __gt__(self, other):
        if self.strength > other.strength:
            return True
        if self.strength < other.strength:
            return False
        return self.cards > other.cards


def main():
    """main"""

    parser = ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    logging.info(args)

    data = Path(args.input).read_text(encoding='utf-8').splitlines()
    #print([Card[f'_{x}'] for x in '77888'] > [Card[f'_{x}'] for x in '77788'])
    #print(Hand('77888', 0) < Hand('78788', 0))

    hands = []
    for line in data:
        cards, bid = line.split()
        hands.append(Hand(cards, int(bid)))

    hands = sorted(hands)
    ranks = range(1, len(hands)+1)
    total = [a * b for a, b in zip([x.bid for x in hands], ranks)]
    print(hands)
    print(f'ans {sum(total)}')


if __name__ == '__main__':
    main()
