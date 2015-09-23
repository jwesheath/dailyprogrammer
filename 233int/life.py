import sys
import random

directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]


def get_num_neighbors(i, j, grid, height, width):
    num_neighbors = 0

    for direction in directions:
        search_i = i + direction[0]
        search_j = j + direction[1]
        if 0 <= search_i < height and 0 <= search_j < width:
                if grid[search_i][search_j] != ' ':
                    num_neighbors += 1

    return num_neighbors


def get_next_state(chars, grid, height, width):
    new_grid = [[' ' for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            num_neighbors = get_num_neighbors(i, j, grid, height, width)
            if grid[i][j] != ' ' and (num_neighbors <= 1 or num_neighbors >= 4):
                new_grid[i][j] = ' '
            elif grid[i][j] != ' ' and num_neighbors in (2, 3):
                new_grid[i][j] = grid[i][j]
            elif grid[i][j] == ' ' and num_neighbors == 3:
                new_grid[i][j] = random.sample(chars, 1)[0]

    return new_grid


def main(argv):
    with open(argv, 'r') as infile:
        lines = [line for line in infile.read().splitlines()]

    chars = set(''.join(lines)) - set(' ')
    height = len(lines)
    width = max([len(line) for line in lines])
    grid = [[char for char in line.ljust(width)] for line in lines]

    new_grid = get_next_state(chars, grid, height, width)

    for line in new_grid:
        print(''.join(line))


if __name__ == '__main__':
    main(sys.argv[1])
