#!/usr/bin/env python3

#My solution for day 6 parts 1 & 2 of the 2025 Advent of Code

p1_total = 0
p2_total = 0
worksheet = []

with open("day6input.txt", 'r') as file:
    for line in file:
        worksheet.append(line.rstrip("\n"))

max_col = max(len(line) for line in worksheet)
num_rows = len(worksheet)

cur_col = 0

while cur_col < max_col:
    nums = []
    max_problem_col_index = cur_col

    for row_index in range(num_rows - 1):
        #searching all rows besides last row, which has the operators on it
        row = worksheet[row_index]
        col_index = cur_col
        num = ""

        if col_index < len(row):
            cont_search = True

            while cont_search:
                if col_index < len(row):
                    char = row[col_index]
                    if char == " " and num != "":
                        #blank space was found and we have a number. go to next row
                        #after adding num to list
                        nums.append(int(num))
                        cont_search = False
                        if col_index > max_problem_col_index:
                            max_problem_col_index = col_index
                    else:
                        #if character isnt space, add char to string to make a number
                        if char != " ":
                            num += char
                else:
                    cont_search = False
                    if num:
                        nums.append(int(num))
                col_index += 1

    if nums:
        #grabbing the operator from the last line now that we have all the numbers going into the equation
        operator = worksheet[-1][cur_col:max_problem_col_index].strip()
        if operator == "+":
            p1_total += sum(nums)
        elif operator == "*":
            product = 1
            for n in nums:
                product *= n
            p1_total += product

    if max_problem_col_index > cur_col:
        cur_col = max_problem_col_index
    else:
        cur_col += 1

print(f'The answer to the homework in part 1 is: {p1_total}')
