#!/usr/bin/env python3
"""
aoc2021 solution skeleton
"""

import logging
from argparse import ArgumentParser
from pathlib import Path


def score_card(winning, ours):
    hits = [x for x in ours if x in winning]
    return len(hits)


def main():
    """main"""

    parser = ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    logging.info(args)

    data = Path(args.input).read_text('utf-8').splitlines()

    cards = {}
    for line in data:
        card_name, card_data = map(str.strip, line.split(':'))
        winning, ours = map(str.split, card_data.split('|'))
        winning = list(map(int, winning))
        ours = list(map(int, ours))
        cards[int(card_name.split(' ')[-1])] = score_card(winning, ours)

    # ha ha ha
#    total = 0
#    buf = list(cards.keys())
#    while buf:
#        cur = buf.pop(0)
#        total += 1
#        cloned = list(range(cur+1, cur+cards[cur]+1))
#        buf += cloned
#        print(len(buf))
#    print(f'ans {total}')

    import json
    print(json.dumps(cards, indent=4))
    totals = {k: 1 for k in cards.keys()}

    for key, val in cards.items():
        cloned = list(range(key+1, key+val+1))

        for idx in cloned:
            totals[idx] += 1 * totals[key]

    print(sum(totals.values()))



if __name__ == '__main__':
    main()
