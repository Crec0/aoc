import util


def read_input(file_name: str) -> list[int]:
    with open(file_name, 'r') as file:
        data = file.readline()
    return [int(elem) for elem in data.split(",")]


def emulate_fish_growth(data: list[int], days: int) -> int:
    TOTAL_COUNTER = 10
    counter = {i: 0 for i in range(TOTAL_COUNTER)}

    for age in data:
        counter[age] += 1

    for day in range(days):
        if counter[0] > 0:
            # offsetting by 1 so the shift can behave nicely
            counter[7] += counter[0]
            counter[9] += counter[0]
        for age in range(1, TOTAL_COUNTER):
            counter[age - 1] = counter[age]
            counter[age] = 0

    return sum(counter.values())


@util.time_it_and_evaluate
def solve_1(data: list[int]) -> int:
    return emulate_fish_growth(data, 80)


@util.time_it_and_evaluate
def solve_2(data: list[int]) -> int:
    return emulate_fish_growth(data, 256)


if __name__ == '__main__':
    # input = read_input('../data/day6/input_example.txt')
    input = read_input('../data/day6/input.txt')
    solve_1(input)
    solve_2(input)
