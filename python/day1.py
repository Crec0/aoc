

from typing import Iterator


def read_input(filename: str) -> list[int]:
    """
    Reads the input and puts it into a parse-able data structure
    :param filename: the name of the file to read
    :return: parsed data
    """
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
    """
    Counts the number of times an element is greater than to its previous element
    :param data: the input data to perform operation on
    :return: number of time element was larger than previous one
    """
    # can be done in one line, but for the sake of readability
    # return sum(curr > prev for prev, curr in zip(data[:-1], data[1:]))

    increase: int = 0

    for prev, curr in zip(data[:-1], data[1:]):
        increase += (curr > prev)

    return increase


def solve_1(data: list[int]) -> int:
    return count_increases(data)


def solve_2(data: list[int]) -> int:
    l = len(data)
    # can be done in one line, but for the sake of readability
    # return count_increases([sum(data[i : i + 3]) for i in range(0, l - l % 3 - 1)])

    triplets: list[int] = []
    for i in range(0, l - l % 3 - 1):
        triplets.append(sum(data[i : i + 3]))
    
    return count_increases(triplets)


if __name__ == '__main__':
    read_data: list[int] = read_input('../data/day1/input.txt')
    ans_1 = solve_1(read_data)
    print(f"{ans_1 = }")

    ans_2 = solve_2(read_data)
    print(f"{ans_2 = }")
