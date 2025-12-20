#!/usr/bin/env python3

#My solution for day 4 parts 1 & 2 of the 2025 Advent of Code

ROLL_CHAR = "@"
MAX_ADJ_ROLLS = 4
p1_accessible_rolls = 0

with open("day4input.txt", 'r') as file:
    roll_coords = set()
    for row_index, line in enumerate(file):
        message = line.strip()
        for col_index, char in enumerate(message):
            if char == ROLL_CHAR:
                roll_coords.add((row_index, col_index))

    for row_index, col_index in roll_coords:
        hits = 0
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                if (row_offset, col_offset) != (0,0):
                    if (row_index + row_offset, col_index + col_offset) in roll_coords:
                        hits += 1
                        if hits == MAX_ADJ_ROLLS:
                            break
            if hits == MAX_ADJ_ROLLS:
                break

        if hits < MAX_ADJ_ROLLS:
            p1_accessible_rolls += 1

print(f'The total number of accessible rolls in part 1 is: {p1_accessible_rolls}')
