#!/usr/bin/env python3

#My solution for day 3 parts 1 & 2 of the 2025 Advent of Code

MAX_BATTERY_JOLTAGE = 9

p1_total_joltage = 0
p2_total_joltage = 0

def max_bank_joltage(joltage_rating: str, num_batteries: int) -> int:
    num_battery_banks = len(joltage_rating)
    output_joltage = ""
    last_char_index = -1

    while num_batteries > 0:
        high_joltage = 0
        char_index = last_char_index + 1

        end_search_index = 0
        if num_batteries == 1:
            end_search_index = num_battery_banks
        else:
            end_search_index = -num_batteries + 1

        for char in joltage_rating[char_index : end_search_index]:
            battery_joltage = int(char)
            if battery_joltage > high_joltage:
                high_joltage = battery_joltage
                last_char_index = char_index
            char_index += 1
            if high_joltage == MAX_BATTERY_JOLTAGE:
                break;

        output_joltage += str(high_joltage)
        num_batteries -= 1

    return int(output_joltage)

with open("day3input.txt", 'r') as file:
    for line in file:
        joltage_rating = line.strip()
        p1_total_joltage += max_bank_joltage(joltage_rating, 2)
        p2_total_joltage += max_bank_joltage(joltage_rating, 12)

print(f'The total output joltage for part 1 is: {p1_total_joltage}')
print(f'The total output joltage for part 2 is: {p2_total_joltage}')
