#!/usr/bin/env python3
"""
aoc2021 solution skeleton
"""

import logging
import operator
from argparse import ArgumentParser
from pathlib import Path

import numpy as np


def get_adjacent_points(point, boundary):
    """uses row,col notation"""
    points = []

    for vector in [(-1,0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (-1, -1), (0, -1)]:
        tmp = tuple(map(operator.add, point, vector))
        if (tmp[0] < 0) or (tmp[0] > boundary[0]-1):
            continue
        if (tmp[1] < 0) or (tmp[1] > boundary[1]-1):
            continue
        points.append(tmp)

    return points


def is_symbol(char):
    if char.isdigit():
        return False
    if char == '.':
        return False
    return True


def main():
    """main"""

    parser = ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    logging.info(args)

    data = Path(args.input).read_text('utf-8').splitlines()
    data = np.array(list(map(list, data)), dtype=str)
    rows, cols = data.shape

    print('data', data)
    print('shape', rows, cols)
    print('corners', data[0,0], data[-1, -1])

    parts = []

    number = ''
    is_part = False

    for r in range(rows):
        for c in range(cols):
            current = (r, c)

            if data[current].isdigit():
                number += data[current]
                if any(is_symbol(data[x]) for x in get_adjacent_points(current, data.shape)):
                       is_part = True
                continue

            if not data[current].isdigit() and number:
                if is_part:
                    parts.append(int(number))
                number = ''
                is_part = False

        if number:
            if is_part:
                parts.append(int(number))
            number = ''
            is_part = False


    print(parts)
    print(f'ans {sum(parts)}')


if __name__ == '__main__':
    main()

