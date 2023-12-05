#!/usr/bin/env python3
"""
aoc2021 solution skeleton
"""

import logging
from argparse import ArgumentParser
import subprocess

import part2_worker


def main():
    """main"""

    parser = ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    logging.info(args)

    seeds, maps = part2_worker.load_input(args.input)

    procs = []

    while seeds:
        seed_start = seeds.pop(0)
        seed_length = seeds.pop(0)

        proc = subprocess.Popen(f'python3 ./part2_worker.py {args.input} {seed_start} {seed_length}', shell=True, stdout=subprocess.PIPE, text=True)
        procs.append(proc)

    for proc in procs:
        proc.wait()

    answers = []
    for proc in procs:
        output = proc.communicate()[0].strip()
        answers.append(int(output.split()[-1]))

    print(f'ans {min(answers)}')


if __name__ == '__main__':
    main()
