import re
import sys
import math
import time
from operator import itemgetter


def distance(coord1, coord2):
    return((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)


def brute_force(coords):
    min_distance = float('inf')
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i != j:
                current_distance = distance(coords[i], coords[j])
                if current_distance < min_distance:
                    min_distance = current_distance
                    closest_coords = (coords[i], coords[j])
    return closest_coords, min_distance


def closest_pair(coords):
    if len(coords) <= 3:
        return brute_force(coords)

    mid_point = len(coords) // 2
    left_closest_pair = closest_pair(coords[:mid_point])
    right_closest_pair = closest_pair(coords[mid_point:])
    min_distance = min(left_closest_pair, right_closest_pair, key = itemgetter(1))

    split_pairs = [coord for coord in coords if abs(coord[0]-coords[mid_point][0]) < min_distance[1]]

    if len(split_pairs) > 1:
        closest_strip_pair = brute_force(split_pairs)
    else:
        closest_strip_pair = (float('inf'), float('inf'))

    final_pair = min(closest_strip_pair, min_distance, key = itemgetter(1))
    return (final_pair)


def main(input_text):

    # Read in and organize points
    with open(input_text, 'r') as infile:
        _ = infile.readline()
        lines = [re.sub(r'[(),\n]', '', line).split(' ')
                 for line in infile.readlines()]

    # Coordinate pairs are sorted by x coordinate
    coords = sorted([(float(x[0]), float(x[1])) for x in lines], key=itemgetter(0))

    # Perform and time brute force
    start = time.clock()
    brute_force_coords = brute_force(coords)
    brute_force_time = time.clock() - start
    print(brute_force_coords[0][0], brute_force_coords[0][1])
    print('Brute force takes ' + str(brute_force_time) + ' seconds.')

    # Perform and time divide and conquer
    start = time.clock()
    closest_pair_coords = closest_pair(coords)
    closest_pair_time = time.clock() - start
    print(closest_pair_coords[0][0], closest_pair_coords[0][1])
    print('Divide and conquer takes ' + str(closest_pair_time) + ' seconds.')

    print('Divide and conquer was ' +
          str(brute_force_time - closest_pair_time) + ' seconds faster.')


if __name__ == '__main__':
    main(sys.argv[1])
