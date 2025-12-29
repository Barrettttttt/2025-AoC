#!/usr/bin/env python3

#My solution for day 8 parts 1 & 2 of the 2025 Advent of Code

import math
import bisect
import collections

NUM_TOP_DISTANCES = 1000

coordinates = []
top_distances = []
all_distances = []
circuits = []

p1_total = 0;
p2_total = 0;

def find_parent(coord_index: int, parent: dict) -> int:
    if parent[coord_index] == coord_index:
        return coord_index
    parent[coord_index] = find_parent(parent[coord_index], parent)
    return parent[coord_index]

with open("day8input.txt", 'r') as file:
    for line in file:
        x, y, z = line.split(",")
        coordinates.append( (int(x), int(y), int(z)) )

num_coordinates = len(coordinates)

for coord_a_index in range(num_coordinates):
    x1, y1, z1 = coordinates[coord_a_index]

    for coord_b_index in range(coord_a_index + 1, num_coordinates):
        x2, y2, z2 = coordinates[coord_b_index]

        distance = math.sqrt( pow((x1 - x2), 2) + pow((y1 - y2), 2) + pow((z1 - z2), 2) )
        coords_dist = (distance, coord_a_index, coord_b_index)

        all_distances.append(coords_dist)

        if len(top_distances) < NUM_TOP_DISTANCES:
            bisect.insort(top_distances, coords_dist)

        elif distance < top_distances[-1][0]:
            top_distances.pop()
            bisect.insort(top_distances, coords_dist)

parent = {}
parent_all = {}

for coord_index in range(num_coordinates):
    parent[coord_index] = coord_index
    parent_all[coord_index] = coord_index

for dist, coord_a_index, coord_b_index in top_distances:
    a_parent = find_parent(coord_a_index, parent)
    b_parent = find_parent(coord_b_index, parent)

    if a_parent != b_parent:
        parent[b_parent] = a_parent

for coord_index in range(num_coordinates):
    circuits.append(find_parent(coord_index, parent))

circuit_connection_counts = collections.Counter(circuits)
sorted_circuits = sorted(circuit_connection_counts.values(), reverse = True)

p1_total = sorted_circuits[0] * sorted_circuits[1] * sorted_circuits[2]

all_distances.sort()

connections_remaining = num_coordinates - 1

for dist, coord_a_index, coord_b_index in all_distances:
    a_parent = find_parent(coord_a_index, parent_all)
    b_parent = find_parent(coord_b_index, parent_all)

    if a_parent != b_parent:
        parent_all[b_parent] = a_parent
        connections_remaining -= 1

        if connections_remaining == 0:
            p2_total = coordinates[coord_a_index][0] * coordinates[coord_b_index][0]
            break

print(f'In part 1 the product of the three largest circuits size is : {p1_total}')
print(f'In part 2 the product of the furthest two x coordinates is : {p2_total}')
