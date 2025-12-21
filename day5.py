#!/usr/bin/env python3

#My solution for day 5 parts 1 & 2 of the 2025 Advent of Code

p1_num_fresh_ingred = 0
p2_num_fresh_ingred_avail = 0
fresh_ingred_id_ranges = []
ids = []

def check_freshness(fresh_ingred_id_ranges: list, id: int) -> bool:
    for fresh_ingred_id_range in fresh_ingred_id_ranges:
        lower_lim, upper_lim = fresh_ingred_id_range
        if lower_lim <= id <= upper_lim:
            return True
    return False

def merge_overlapping_ranges(fresh_ingred_id_ranges: list) -> list:
    fresh_ingred_id_ranges.sort()
    merged_fresh_ingred_id_ranges = [fresh_ingred_id_ranges[0]]
    for cur_lower, cur_upper in fresh_ingred_id_ranges[1:]:
        last_lower, last_upper = merged_fresh_ingred_id_ranges[-1]
        if cur_lower <= last_upper:
            new_upper = max(cur_upper, last_upper)
            merged_fresh_ingred_id_ranges[-1] = (last_lower, new_upper)
        else:
            merged_fresh_ingred_id_ranges.append((cur_lower, cur_upper))
    return merged_fresh_ingred_id_ranges

with open("day5input.txt", 'r') as file:
    for line in file:
        message = line.strip()
        if message != "":
            if "-" in message:
                lower_lim, upper_lim = message.split("-")
                fresh_ingred_id_ranges.append((int(lower_lim), int(upper_lim)))
            else:
                ids.append(int(message))

merged_fresh_ingred_id_ranges = merge_overlapping_ranges(fresh_ingred_id_ranges)
lowest_id = merged_fresh_ingred_id_ranges[0][0]
highest_id = merged_fresh_ingred_id_ranges[-1][1]

for id in ids:
    if lowest_id <= id <= highest_id:
        if check_freshness(merged_fresh_ingred_id_ranges, id):
            p1_num_fresh_ingred += 1

for fresh_ingred_id_range in merged_fresh_ingred_id_ranges:
    lower_lim, upper_lim = fresh_ingred_id_range
    p2_num_fresh_ingred_avail += (upper_lim - lower_lim) + 1

print(f'The total number of fresh ingrediants in part 1 is: {p1_num_fresh_ingred}')
print(f'The total number of fresh ingrediants available in part 2 is: {p2_num_fresh_ingred_avail}')
