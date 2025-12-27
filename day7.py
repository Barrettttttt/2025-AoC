#!/usr/bin/env python3

#My solution for day 7 parts 1 & 2 of the 2025 Advent of Code

START_CHAR = "S"
SPLIT_CHAR = "^"
SPACE_CHAR = "."

p1_total = 0
p2_total = 0

beam_cols = []
timelines_by_splitter= {}

with open("day7input.txt", 'r') as file:
    for line in file:
        new_beam_cols = []
        new_timelines = {}

        if START_CHAR in line:
            beam_cols.append(line.index(START_CHAR))
            timelines_by_splitter[line.index(START_CHAR)] = 1

        if SPLIT_CHAR in line:
            #not sure if we can have start and splits in the same line. allowing it for now.
            for col_index in beam_cols:
                char = line[col_index]
                timeline_count = timelines_by_splitter[col_index]

                if char == SPLIT_CHAR:
                    p1_total += 1
                    left_split_index = col_index - 1
                    right_split_index = col_index + 1
                    #make sure we aren't going outside the graph we were given
                    if left_split_index >= 0:
                        new_beam_cols.append(left_split_index)
                        if left_split_index not in new_timelines:
                            new_timelines[left_split_index] = 0
                        new_timelines[left_split_index] += timeline_count
                    if right_split_index < len(line):
                        new_beam_cols.append(right_split_index)
                        if right_split_index not in new_timelines:
                            new_timelines[right_split_index] = 0
                        new_timelines[right_split_index] += timeline_count

                else:
                    #no splitter at the index where an existing beam is passing 
                    #still shooting straight down the graph. make sure beams still going down next pass
                    new_beam_cols.append(col_index)
                    if col_index not in new_timelines:
                        new_timelines[col_index] = 0
                    new_timelines[col_index] += timeline_count
            beam_cols = new_beam_cols
            timelines_by_splitter = new_timelines


        beam_cols = list(set(beam_cols))

p2_total = sum(timelines_by_splitter.values())

print(f'In part 1 the beam split : {p1_total} times')
print(f'In part 2 the beam split : {p2_total} times')
