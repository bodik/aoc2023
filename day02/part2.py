#!/usr/bin/env python3

import sys
from pathlib import Path
from dataclasses import dataclass


CONSTRAINT_RED = 12
CONSTRAINT_GREEN = 13
CONSTRAINT_BLUE = 14


def list_to_mapping(key_val_list):
    # Check if the list has an even number of elements
    if len(key_val_list) % 2 != 0:
        raise ValueError("The list should contain an even number of elements")

    # Creating a mapping from the list
    mapping = {key_val_list[i]: int(key_val_list[i + 1]) for i in range(0, len(key_val_list), 2)}
    return mapping


@dataclass
class Draw:
    red: int = 0
    green: int = 0
    blue: int = 0


def parse_game_draws(draws):
    return [
        Draw(**list_to_mapping(list(reversed(drawdata.strip().replace(',', '').split(' ')))))
        for drawdata
        in draws.split(';')
    ]

def game_power(draws):

    red_power = max([x.red for x in draws])
    green_power = max([x.green for x in draws])
    blue_power = max([x.blue for x in draws])

    return red_power * green_power * blue_power


def main():
    """main"""
    
    ans = 0

    data = Path(sys.argv[1]).read_text().splitlines()
    for line in data:
        game_name, game_draws = line.split(':')
        game_number = int(game_name.split(' ')[-1])

        parsed_draws = parse_game_draws(game_draws)
        parsed_power = game_power(parsed_draws)
        
        #print(line)
        #print(parsed_draws)
        #print(parsed_power)

        ans += parsed_power

    print(f'answer {ans}')


if __name__ == '__main__':
    main()
