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

    for vector in [NORTH, EAST, SOUTH, WEST]:
        tmp = tuple(map(operator.add, point, vector))
        if (tmp[0] < 0) or (tmp[0] > boundary[0]-1):
            continue
        if (tmp[1] < 0) or (tmp[1] > boundary[1]-1):
            continue
        points.append(tmp)

    return points


def move(point, direction):
    return tuple(map(operator.add, point, direction))


def swap(direction):
    return tuple(map(operator.mul, direction, (-1, -1)))


def detect_loop(data, start):

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

    assert swap(NORTH) == SOUTH
    assert swap(SOUTH) == NORTH
    assert swap(EAST) == WEST

    # ! missing check if start field os not on the edge of map
    
    # start north
    for direction in NORTH, SOUTH, EAST, WEST:
        new_point = move(start, direction)
        incoming = swap(direction)
        if incoming in can_connect[data[new_point]]:

            current, path = start, [start]
            while True:
                new_point = move(current, direction)
                new_point_content = data[new_point]
                if new_point_content == 'S':
                    return path + [new_point]

                if incoming not in can_connect[new_point_content]:
                    break
                
                new_direction = can_connect[data[new_point]].copy()
                new_direction.remove(incoming)
                direction = new_direction[0]
                incoming = swap(direction)
                current = new_point
                path.append(current)

    raise RuntimeError('path not found')


def main():
    """main"""

    parser = ArgumentParser()
#    parser.add_argument('input')
#    args = parser.parse_args()
#    logging.info(args)

    data = Path('/workspaces/aoc2023/day10/input.test1').read_text('utf-8').splitlines()
    data = np.array(list(map(list, data)), dtype=str)
    rows, cols = data.shape
    start = np.where(data=='S')
    start = (start[0][0], start[1][0])

    print('data\n', data)
    print('shape', rows, cols)
    print('corners', data[0,0], data[-1, -1])
    print('start', start)

    path = detect_loop(data, start)
    print(path)
    print(f'ans {(len(path)-1)/2}')


if __name__ == '__main__':
    main()

