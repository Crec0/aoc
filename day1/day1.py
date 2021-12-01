
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


def count_increases(data: list[int]) -> int:
    """
    Counts the number of times an element is greater than to its previous element
    :param data: the input data to perform operation on
    :return: number of time element was larger than previous one
    """
    prev: int = data[0]
    increase: int = 0

    for curr in data[1:]:
        increase += (curr > prev)
        prev = curr

    return increase


def solve_1(data: list[int]) -> int:
    return count_increases(data)


def solve_2(data: list[int]) -> int:
    prev_1: int = data[0]
    prev_2: int = data[1]
    prev_3: int = data[2]

    sums_of_3: list[int] = [prev_1 + prev_2 + prev_3]

    for curr in data[3:]:
        prev_1 = prev_2
        prev_2 = prev_3
        prev_3 = curr
        sums_of_3.append(prev_1 + prev_2 + prev_3)

    return count_increases(sums_of_3)


if __name__ == '__main__':
    read_data: list[int] = read_input('input_1.txt')
    ans_1 = solve_1(read_data)
    print(f"{ans_1 = }")
    ans_2 = solve_2(read_data)
    print(f"{ans_2 = }")
