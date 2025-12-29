#!/usr/bin/env python3

#My solution for day 9 parts 1 & 2 of the 2025 Advent of Code

red_tile_coords = []
p1_largest_area = 0

def find_rect_area(x1 : int, x2 : int, y1 : int, y2 : int) -> int:
    len_rect = abs(x1-x2) + 1
    width_rect = abs(y1-y2) + 1

    return len_rect * width_rect

with open("day9input.txt", 'r') as file:
    for line in file:
        x, y = line.split(",")
        red_tile_coords.append( (int(x), int(y)) )

num_red_tiles = len(red_tile_coords)

for tile_a_index in range(num_red_tiles):
    x1, y1 = red_tile_coords[tile_a_index]

    for tile_b_index in range(tile_a_index + 1, num_red_tiles):
        x2, y2 = red_tile_coords[tile_b_index]

        area = find_rect_area(x1, x2, y1, y2)

        if area > p1_largest_area:
            p1_largest_area = area

print(f"The largest area between two red tiles in part 1 is: {p1_largest_area}")
