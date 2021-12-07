import math
import statistics


def read_input(file_name: str) -> list[int]:
    with open(file_name, 'r') as file:
        data = file.readline()
    return [int(elem) for elem in data.split(",")]


def solve_1(data: list[int]) -> int:
    cheapest = statistics.median(data)
    return sum(abs(elem - cheapest) for elem in data)


def solve_2(data: list[int]) -> int:
    pos = math.floor(statistics.mean(data))
    return sum(map(lambda n: n / 2 * (n + 1), map(lambda e: abs(e - pos), data)))


if __name__ == '__main__':
    # input = read_input('../data/day7/input_example.txt')
    input = read_input('../data/day7/input.txt')
    ans_1 = solve_1(input)
    print(f"{ans_1 = }")

    ans_2 = solve_2(input)
    print(f"{ans_2 = }")
