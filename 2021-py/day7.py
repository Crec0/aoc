import math
import statistics

import util


def read_input(file_name: str) -> list[int]:
    with open(file_name, 'r') as file:
        data = file.readline()
    return [int(elem) for elem in data.split(",")]


@util.time_it_and_evaluate
def solve_1(data: list[int]) -> int:
    cheapest = statistics.median(data)
    return sum(abs(elem - cheapest) for elem in data)


@util.time_it_and_evaluate
def solve_2(data: list[int]) -> int:
    pos = math.floor(statistics.mean(data))
    return sum(map(lambda n: n / 2 * (n + 1), map(lambda e: abs(e - pos), data)))


if __name__ == '__main__':
    input = read_input('../data/day7/input.txt')
    solve_1(input)
    solve_2(input)
