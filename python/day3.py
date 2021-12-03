

def read_input(filename: str) -> list[str]:
    input_data: list[str] = []
    with open(filename, 'r') as input_file:
        for line in input_file.readlines():
            input_data.append(line.strip())
    return input_data

def count_ones_in_column(data: list[str], index: int) -> int:
    ones = 0
    for num in data:
        ones += 1 * num[index] == '1'
    return ones


def get_common_bit(total_size: int, ones: int, match_most: bool) -> str:
    zeros = total_size - ones
    if ones >= zeros:
        return '1' if match_most else '0'
    else:
        return '0' if match_most else '1'

    # unreadable xnor which also works
    # return str(1 * (True - ((ones >= zeros) ^ match_most)))


def common_counter(data: list[str], most_common: bool, depth: int = 0):
    if depth == len(data[0]):
        return ''

    ones = count_ones_in_column(data, depth)
    common_bit = get_common_bit(len(data), ones, most_common)

    return common_bit + common_counter(data, most_common, depth + 1)


def solve_1(data: list[str]) -> int:
    gamma = common_counter(data, True)
    epsilon = common_counter(data, False)
    return int(gamma, base=2) * int(epsilon, base=2)


def common_reduction(data: list[str], most_common: bool, depth: int = 0):
    if len(data) == 1:
        return data[0]

    ones = count_ones_in_column(data, depth)
    common_bit = get_common_bit(len(data), ones, most_common)

    return common_reduction([digit for digit in data if digit[depth] == common_bit], most_common, depth + 1)


def solve_2(data: list[str]) -> int:
    oxygen = common_reduction(data, True)
    carbon = common_reduction(data, False)
    return int(oxygen, base=2) * int(carbon, base=2)


if __name__ == '__main__':
    read_data = read_input('../data/day3/input.txt')
    ans_1 = solve_1(read_data)
    print(f"{ans_1 = }")

    ans_2 = solve_2(read_data)
    print(f"{ans_2 = }")
