#!/usr/bin/env python3

#My solution for day 3 parts 1 & 2 of the 2025 Advent of Code

total_joltage = 0
max_battery_joltage = 9

with open("day3input.txt", 'r') as file:
    for line in file:
        joltage_rating = line.strip()

        cur_high_jolt = 0
        cur_high_jolt_indx = 0
        num_battery_banks = len(joltage_rating)

        #purposely leaving out the last digit in the joltage rating since we need a 2 digit number
        for char_index in range(num_battery_banks - 1):
            battery_joltage = int(joltage_rating[char_index])
            if battery_joltage > cur_high_jolt:
                cur_high_jolt = battery_joltage
                cur_high_jolt_indx = char_index
                if cur_high_jolt == max_battery_joltage:
                    break

        sec_battery_joltage = 0

        for char_index in range(cur_high_jolt_indx + 1, num_battery_banks):
            battery_joltage = int(joltage_rating[char_index])
            if battery_joltage > sec_battery_joltage:
                sec_battery_joltage = battery_joltage

        total_joltage += (cur_high_jolt * 10) + sec_battery_joltage


print(f'The total output joltage for part 1 is: {total_joltage}')
