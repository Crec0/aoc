from itertools import tee, pairwise
from typing import Iterator


def read_input(filename: str) -> list[int]:
    input_data: list[int] = []
    with open(filename, 'r') as input_file:
        input_data.extend(
            map(
                lambda line: int(line.strip()),
                input_file.readlines()
            )
        )
    return input_data


def count_increases(data: list[int] | Iterator[int]) -> int:
    return sum(curr > prev for prev, curr in pairwise(data))


def solve_1(data: list[int]) -> int:
    return count_increases(data)


def tripletwise(data: list[int]) -> Iterator:
    it1, it2, it3 = tee(data, 3)
    # consume it2 once
    next(it2, None)
    # consume it3 twice
    next(it3, None)
    next(it3, None)
    # now we can zip by shortest (it3)
    # this will be now [(e1, e2, e2), (e2, e3, e4), ...]
    return zip(it1, it2, it3)


def solve_2(data: list[int]) -> int:
    return count_increases(sum(triple) for triple in tripletwise(data))


if __name__ == '__main__':
    read_data: list[int] = read_input('./data/day1/input.txt')
    ans_1 = solve_1(read_data)
    print(f"{ans_1 = }")

    ans_2 = solve_2(read_data)
    print(f"{ans_2 = }")
