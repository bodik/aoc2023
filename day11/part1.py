#!/usr/bin/env python3
"""
aoc2021 solution skeleton
"""

import logging
import operator
from argparse import ArgumentParser
from pathlib import Path
import subprocess

import numpy as np

NORTH = (-1, 0)
SOUTH = (1, 0)
WEST = (0, -1)
EAST = (0, 1)


def debug_print_path(data, path):
    xdata = data.copy()
    for xpoint in path:
        xdata[xpoint] = 'x'
    print(xdata)


def debug_trace_path(data, path):
    xdata = data.copy()
    for xpoint in path:
        xdata[xpoint] = 'x'

    trace_data = ''
    for row in xdata:
        trace_data += ''.join(row) + '\n'
    trace = Path('trace.log')
    trace.unlink(missing_ok=True)
    trace.write_text(trace_data)
    subprocess.run('less trace.log', shell=True)
    

def get_adjacent_points(point, boundary):
    """uses row,col notation"""
    points = []

    for vector in [(-1,0), (0, 1), (1, 0), (0, -1)]:
        tmp = tuple(map(operator.add, point, vector))
        if (tmp[0] < 0) or (tmp[0] > boundary[0]-1):
            continue
        if (tmp[1] < 0) or (tmp[1] > boundary[1]-1):
            continue
        points.append(tmp)

    return points


def detect_loop(data, point, path):

    can_connect = {
        # | is a vertical pipe connecting north and south.
        '|': [NORTH, SOUTH],
        # - is a horizontal pipe connecting east and west.
        '-': [WEST, EAST],
        # L is a 90-degree bend connecting north and east.
        'L': [NORTH, EAST],
        # J is a 90-degree bend connecting north and west.
        'J': [NORTH, WEST],
        # 7 is a 90-degree bend connecting south and west.
        '7': [SOUTH, WEST],
        # F is a 90-degree bend connecting south and east.
        'F': [SOUTH, EAST],
        # . is ground; there is no pipe in this tile.
        '.': [],
    }

    print(f'DEBUG: path {path}')
    adjacent = get_adjacent_points(point, data.shape)
    print(f'DEBUG: current {point} adj {adjacent}')
    for new_point in adjacent:
        direction = tuple(map(operator.sub, new_point, point))
        new_point_content = data[new_point]

        if len(path) > 1 and new_point_content == 'S':
            return path + [point]

        if new_point in path:
            continue

        if (direction == NORTH) and (SOUTH in can_connect[new_point_content]):
            pass
        elif (direction == SOUTH) and (NORTH in can_connect[new_point_content]):
            pass
        elif (direction == WEST) and (EAST in can_connect[new_point_content]):
            pass
        elif (direction == EAST) and (WEST in can_connect[new_point_content]):
            pass
        else:
            continue

        try:
            debug_print_path(data, path + [new_point])
#            debug_trace_path(data, path + [new_point])
            return detect_loop(data, new_point, path + [new_point])
        except RuntimeError:
            continue

    print('DEBUG: failed to find correct next point')
    raise RuntimeError('loop detection failed')


def main():
    """main"""

    parser = ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    logging.info(args)

    data = Path(args.input).read_text('utf-8').splitlines()
    data = np.array(list(map(list, data)), dtype=str)
    rows, cols = data.shape
    start = np.where(data=='S')
    start = (start[0][0], start[1][0])

    print('data\n', data)
    print('shape', rows, cols)
    print('corners', data[0,0], data[-1, -1])
    print('start', start)

    path = detect_loop(data, start, [start])
    print(path)
    print(f'ans {(len(path)-1)/2}')


if __name__ == '__main__':
    main()

