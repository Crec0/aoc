from itertools import pairwise

import util


def parse_input_data(filename):
    return [int(line.strip()) for line in util.read_all_lines(filename)]


def count_increases(data):
    return sum(curr > prev for prev, curr in pairwise(data))


@util.time_it_and_evaluate
def solve_1(data):
    return count_increases(data)


@util.time_it_and_evaluate
def solve_2(data):
    return count_increases(sum(triple) for triple in util.triplewise(data))


if __name__ == '__main__':
    # read_data = parse_input_data('../data/day1/input_example.txt')
    read_data = parse_input_data('../data/day1/input.txt')

    solve_1(read_data)
    solve_2(read_data)
