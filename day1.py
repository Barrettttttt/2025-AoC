#!/usr/bin/env python3

#My solution for day 1 parts 1 & 2 of the 2025 Advent of Code

pos = 50
max_pos = 99
min_pos = 0
dial_nums = (max_pos - min_pos) + 1
target_num = 0

p1_count = 0
p2_count = 0

with open("input.txt", 'r') as file:
    for line in file:

        message = line.strip()
        direction = message[0]
        distance = int(message[1:])

        if (direction == "L" or direction == "R") and distance > 0:

            hits = 0

            if direction == "R":
                hits = (pos + distance) // dial_nums
                pos = (pos + distance) % dial_nums

            elif direction == "L":
                hits = (distance + (dial_nums - pos) % dial_nums) // dial_nums
                pos = (pos - distance) % dial_nums

            if pos == target_num:
                p1_count += 1

            p2_count += hits

print(f"Part 1 count: {p1_count}")
print(f"Part 2 count: {p2_count}")
