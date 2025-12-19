#!/usr/bin/env python3

#My solution for day 2 parts 1 & 2 of the 2025 Advent of Code

p1_invalid_ids_sum = 0
p2_invalid_ids_sum = 0

def p1_validity_check(id: str) -> bool:
    num_chars = len(id)
    if num_chars % 2 != 0:
        return False
    else:
        if id[0:num_chars//2] == id[num_chars//2:]:
            return True

def p2_validity_check(id: str) -> bool:
    num_chars = len(id)
    for pattern_len in range(1, (num_chars//2) + 1):
        if num_chars % pattern_len == 0:
            pattern = id[:pattern_len]
            if pattern * (num_chars // pattern_len) == id:
                return True
    return False

with open("day2input.txt", 'r') as file:
    for line in file:
        id_ranges = line.strip().split(',')
        for id_set in id_ranges:
            first_id, last_id = id_set.split('-')
            for id in range(int(first_id), int(last_id) + 1):
                if p1_validity_check(str(id)):
                    p1_invalid_ids_sum += id
                if p2_validity_check(str(id)):
                    p2_invalid_ids_sum += id

print(f"The sum of invalid ids in part 1 is: {p1_invalid_ids_sum}")
print(f"The sum of invalid ids in part 2 is: {p2_invalid_ids_sum}")
