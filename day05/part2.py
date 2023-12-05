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

    def translate(self, values):
        results = []

        for value in values:
            for irange in self.ranges:
                if (value >= irange.src_begin) and (value < irange.src_end):
                    results.append(irange.dest + (value - irange.src_begin))
                    break
            else:
                results.append(value)

        return results

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

    location = None
    while seeds:
        seed_start = seeds.pop(0)
        seed_length = seeds.pop(0)

        tmps = list(range(seed_start, seed_start + seed_length))
        for imap_name, imap in maps.items():
            tmps = imap.translate(tmps)

        current_min = min(tmps)
        location = min(current_min, location) if location else current_min
        print(len(seeds))

    print(f'ans {location}')


if __name__ == '__main__':
    main()
