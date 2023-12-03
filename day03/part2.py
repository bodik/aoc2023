#!/usr/bin/env python3
"""
aoc2021 solution skeleton
"""

import logging
import operator
from argparse import ArgumentParser
from pathlib import Path

import numpy as np


class Partnum:
    def __init__(self):
        self.number = ''
        self.points = []
        self.is_part = False

    def add_digit(self, val, point):
        self.number += val
        self.points.append(point)

    def __repr__(self):
        return f'Part({self.number}, {self.points})'


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
    part = Partnum()

    for r in range(rows):
        for c in range(cols):
            current = (r, c)

            if data[current].isdigit():
                part.add_digit(data[current], current)
                if any(is_symbol(data[x]) for x in get_adjacent_points(current, data.shape)):
                       part.is_part = True
                continue

            if not data[current].isdigit() and part.number:
                if part.is_part:
                    parts.append(part)
                part = Partnum()

        if part.number:
            if part.is_part:
                parts.append(part)
            part = Partnum()

    print(f'ans part1 {sum([int(x.number) for x in parts])}')
    print(parts)

    ans = 0

    for r in range(rows):
        for c in range(cols):
            current = (r, c)

            if data[current] == '*':  # is_gear()
                gear_parts = []

                for point in get_adjacent_points(current, data.shape):
                    for part in parts:
                        if point in part.points:
                            gear_parts.append(part)

                gear_parts = list(set(gear_parts))
                if len(gear_parts) == 2:
                    ans += int(gear_parts[0].number) * int(gear_parts[1].number)

                print(current, gear_parts)

    print(f'ans part2 {ans}')



if __name__ == '__main__':
    main()

