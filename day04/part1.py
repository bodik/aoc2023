#!/usr/bin/env python3
"""
aoc2021 solution skeleton
"""

import logging
from argparse import ArgumentParser
from pathlib import Path


def score_card(winning, ours):
    hits = [x for x in ours if x in winning]

    if not hits:
        return 0

    if len(hits) == 1:
        return 1

    buf = 1
    for i in range(len(hits)-1):
        buf = buf*2

    return buf


def main():
    """main"""

    parser = ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    logging.info(args)

    data = Path(args.input).read_text('utf-8').splitlines()

    ans = 0
    for line in data:
        card_name, card_data = map(str.strip, line.split(':'))
        winning, ours = map(str.split, card_data.split('|'))
        winning = list(map(int, winning))
        ours = list(map(int, ours))

        ans += score_card(winning, ours)

    print(f'ans {ans}')


if __name__ == '__main__':
    main()

