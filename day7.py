#!/usr/bin/env python3

#My solution for day 7 parts 1 & 2 of the 2025 Advent of Code

START_CHAR = "S"
SPLIT_CHAR = "^"
SPACE_CHAR = "."

p1_total = 0
p2_total = 0

beam_cols = []

with open("day7input.txt", 'r') as file:
    for line in file:
        new_beam_cols = []

        if START_CHAR in line:
            beam_cols.append(line.index(START_CHAR))

        if SPLIT_CHAR in line:
            #not sure if we can have start and splits in the same line. allowing it for now.
            for col_index in beam_cols:
                char = line[col_index]

                if char == SPLIT_CHAR:
                    p1_total += 1
                    left_split_index = col_index - 1
                    right_split_index = col_index + 1
                    if left_split_index >= 0:
                        new_beam_cols.append(left_split_index)
                    if right_split_index < len(line):
                        new_beam_cols.append(right_split_index)
                else:
                    new_beam_cols.append(col_index)
            beam_cols = new_beam_cols

        else:
            beam_cols = beam_cols
            
        beam_cols = list(set(beam_cols))

print(f'In part 1 the beam split : {p1_total} times')
print(f'In part 2 the beam split : {p2_total} times')
