from itertools import chain
import util

def read_input(filename: str) -> tuple[list, int, int]:
    with open(filename, 'r') as input_file:
        read_input_data = [
            int(elem)
            for line in input_file.readlines()
            for sublist in line.strip().split(' -> ')
            for elem in sublist.split(',')
        ]
    coords = [[], [], [], []]  # x1 y1 x2 y2

    minimum = min(read_input_data)
    maximum = max(read_input_data)

    for i, val in enumerate(read_input_data):
        coords[i % 4].append(val)

    return coords, minimum, maximum


def make_grid(mini: int, maxi: int):
    return [[0] * (mini + maxi + 1) for _ in range(mini + maxi + 1)]

@util.time_it_and_evaluate
def solve_1(data: list, grid: list) -> int:
    for x1, y1, x2, y2 in zip(*data):
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)
        if x1 == x2:
            for y in range(y_min, y_max + 1):
                grid[y][x_min] += 1
        elif y1 == y2:
            for x in range(x_min, x_max + 1):
                grid[y_min][x] += 1
    return len([x for x in chain(*grid) if x > 1])


def print_grid(grid):
    print('\n'.join([' '.join(map(str, ['.' if elem == 0 else elem for elem in row])) for row in grid]), end='\n\n')

@util.time_it_and_evaluate
def solve_2(data: list, grid: list) -> int:
    for x1, y1, x2, y2 in zip(*data):
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)

        if x1 == x2:
            for y in range(y_min, y_max + 1):
                grid[y][x1] += 1

        elif y1 == y2:
            for x in range(x_min, x_max + 1):
                grid[y1][x] += 1

        elif x_max - x_min == y_max - y_min:
            m = (y2 - y1) // (x2 - x1)
            b = y1 - m * x1
            for x in range(x_min, x_max + 1):
                grid[m * x + b][x] += 1

    return len([x for x in chain(*grid) if x > 1])


if __name__ == '__main__':
    # read_data, mini, maxi = read_input('../data/day5/input_example.txt')
    read_data, mini, maxi = read_input('../data/day5/input.txt')
    empty_grid = make_grid(mini, maxi)
    solve_1(read_data, empty_grid)

    empty_grid2 = make_grid(mini, maxi)
    solve_2(read_data, empty_grid2)
