#!/usr/bin/env python3

#My solution for day 4 parts 1 & 2 of the 2025 Advent of Code

ROLL_CHAR = "@"
MAX_ADJ_ROLLS = 4
p1_accessible_rolls = 0
p2_accessible_rolls = 0

def find_accessible_rolls(roll_coords: set, remove_rolls: bool) -> int:
    accessible_rolls_found = 0
    removed_rolls = set()
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
            accessible_rolls_found += 1
            removed_rolls.add((row_index, col_index))
    if remove_rolls:
        for roll in removed_rolls:
            roll_coords.discard(roll)
    return accessible_rolls_found

with open("day4input.txt", 'r') as file:
    roll_coords = set()
    for row_index, line in enumerate(file):
        message = line.strip()
        for col_index, char in enumerate(message):
            if char == ROLL_CHAR:
                roll_coords.add((row_index, col_index))
    p1_accessible_rolls += find_accessible_rolls(roll_coords, False)
    while (True):
        rolls_removed = find_accessible_rolls(roll_coords, True)
        if rolls_removed == 0:
            break
        else:
            p2_accessible_rolls += rolls_removed


print(f'The total number of accessible rolls in part 1 is: {p1_accessible_rolls}')
print(f'The total number of accessible rolls in part 2 is: {p2_accessible_rolls}')
