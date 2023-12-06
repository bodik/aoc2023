#!/usr/bin/env python3
"""
aoc2021 solution skeleton
"""

import logging
import math
from argparse import ArgumentParser
from pathlib import Path


def main():
    """main"""

    parser = ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    logging.info(args)

    data = Path(args.input).read_text(encoding='utf-8').splitlines()

    times = [int(''.join(data[0].split()[1:]))]
    distances = [int(''.join(data[1].split()[1:]))]
    print(times)
    print(distances)

    # times [7, 15, 30]
    # distance [9, 40, 200]

    ans = []
    for idx in range(len(times)):
        wins = 0

        for hold_time in range(times[idx]):
            travel_time = times[idx] - hold_time
            distance = travel_time * hold_time
            if distance > distances[idx]:
                wins += 1

        ans.append(wins)

    print(f'ans {math.prod(ans)}')


if __name__ == '__main__':
    main()
