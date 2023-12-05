#!/usr/bin/env python3
"""
aoc2021 solution skeleton
"""

import logging
from argparse import ArgumentParser
from pathlib import Path


class MapRange:
    def __init__(self, dest, src, size):
        self.dest = dest
        self.src_begin = src
        self.src_end = src + size


class Map:
    def __init__(self, name):
        self.name = name
        self.ranges = []

    def add_range(self, *args):
        self.ranges.append(MapRange(*args))

    def translate(self, value):
        for irange in self.ranges:
            if (value >= irange.src_begin) and (value < irange.src_end):
                return irange.dest + (value - irange.src_begin)

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


def compute_seed_set(seed_start, seed_length, maps):
    location = None
    
    for seed in range(seed_start, seed_start + seed_length):
        tmp = seed
        for imap_name, imap in maps.items():
            tmp = imap.translate(tmp)
        location = min(tmp, location) if location else tmp

    print(f'ans {seed_start} {seed_length} {location}')


def main():
    """main"""

    parser = ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('seed_start', type=int)
    parser.add_argument('seed_length', type=int)
    args = parser.parse_args()
    logging.info(args)

    seeds, maps = load_input(args.input)

    compute_seed_set(args.seed_start, args.seed_length, maps)


if __name__ == '__main__':
    main()
