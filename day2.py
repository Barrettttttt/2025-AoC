#!/usr/bin/env python3

#My solution for day 2 parts 1 & 2 of the 2025 Advent of Code

invalid_ids_sum = 0

def is_invalid(id: str) -> bool:
    num_chars = len(id)
    if num_chars % 2 != 0:
        return False
    else:
        if id[0:num_chars//2] == id[num_chars//2:]:
            return True

with open("day2input.txt", 'r') as file:
    for line in file:
        id_ranges = line.strip().split(',')
        for id_set in id_ranges:
            first_id, last_id = id_set.split('-')
            for id in range(int(first_id), int(last_id) + 1):
                if is_invalid(str(id)):
                    invalid_ids_sum += id

print(f"The sum of invalid ids is: {invalid_ids_sum}")
