#!/usr/bin/env python3
"""
aoc2021 solution skeleton
"""

import logging
from argparse import ArgumentParser
from pathlib import Path
from collections import namedtuple


MapRange = namedtuple('MapRange', ['dest', 'src', 'size'])


class Map:
    def __init__(self, name):
        self.name = name
        self.ranges = []

    def add_range(self, *args):
        self.ranges.append(MapRange(*args))

    def translate(self, value):
        for irange in self.ranges:
            if (value >= irange.src) and (value < irange.src+irange.size):
                return irange.dest + (value - irange.src)
        return value

    def __repr__(self):
        return f'Map({self.name}, {self.ranges}'


def load_input(filename):
    data = Path(filename).read_text('utf-8').splitlines()

    seeds = None
    map_name = None
    maps = {}

    for line in data:
        if not line:
            continue

        if line.startswith('seeds:'):
            seeds = list(map(int, line.split(' ')[1:]))
            continue

        if line.endswith('map:'):
            map_name = line.split(' ')[0]
            maps[map_name] = Map(map_name)
            continue

        maps[map_name].add_range(*map(int, line.split(' ')))

    return seeds, maps


def main():
    """main"""

    parser = ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    logging.info(args)

    seeds, maps = load_input(args.input)

    print(seeds)
    print(maps)

    locations = []
    for seed in seeds:
        tmp = seed
        for imap_name, imap in maps.items():
            tmp = imap.translate(tmp)
        print(seed, tmp)
        locations.append(tmp)

    print(f'ans {min(locations)}')


if __name__ == '__main__':
    main()
