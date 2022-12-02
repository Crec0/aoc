import util


def parse_input_data(filename):
    input_data = []
    for line in util.read_all_lines(filename):
        command, amount = line.split(' ')
        input_data.append((command, int(amount)))
    return input_data


@util.time_it_and_evaluate
def solve_1(data):
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


@util.time_it_and_evaluate
def solve_2(data):
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
    read_data = parse_input_data('../data/day2/input.txt')
    solve_1(read_data)
    solve_2(read_data)
