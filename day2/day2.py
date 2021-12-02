def read_input(filename: str) -> list[tuple[str, int]]:
    """
    Reads the input and puts it into a parse-able data structure
    :param filename: the name of the file to read
    :return: parsed data
    """
    input_data: list[tuple[str, int]] = []
    with open(filename, 'r') as input_file:
        for line in input_file.readlines():
            command, amount = line.split(' ')
            input_data.append((command, int(amount)))
    return input_data


def solve_1(data: list[tuple[str, int]]) -> int:
    h_pos = depth = 0

    for command, amount in data:
        match command:
            case 'forward':
                h_pos += amount
            case 'down':
                depth += amount
            case 'up':
                depth -= amount

    return h_pos * depth

def solve_2(data: list[tuple[str, int]]) -> int:
    h_pos = depth = aim = 0

    for command, amount in data:
        match command:
            case 'forward':
                h_pos += amount
                depth += aim * amount
            case 'down':
                aim += amount
            case 'up':
                aim -= amount

    return h_pos * depth


if __name__ == '__main__':
    read_data = read_input('input_1.txt')
    ans_1 = solve_1(read_data)
    print(f"{ans_1 = }")
    ans_2 = solve_2(read_data)
    print(f"{ans_2 = }")
