#!/usr/bin/env python3

#My solution for day 5 parts 1 & 2 of the 2025 Advent of Code

p1_num_fresh_ingred = 0
fresh_ingred_id_ranges = []
ids = []

def check_freshness(fresh_ingred_id_ranges: list, id: int) -> bool:
    for fresh_ingred_id_range in fresh_ingred_id_ranges:
        lower_lim, upper_lim = fresh_ingred_id_range
        if lower_lim <= id <= upper_lim:
            return True
    return False

with open("day5input.txt", 'r') as file:
    for line in file:
        message = line.strip()
        if message != "":
            if "-" in message:
                lower_lim, upper_lim = message.split("-")
                fresh_ingred_id_ranges.append((int(lower_lim), int(upper_lim)))
            else:
                ids.append(int(message))

for id in ids:
    if check_freshness(fresh_ingred_id_ranges, id):
        p1_num_fresh_ingred += 1

print(f'The total number of fresh ingrediants in part 1 is: {p1_num_fresh_ingred}')
