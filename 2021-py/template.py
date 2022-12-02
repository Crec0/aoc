import util


def parse_input_data(file_name):
    read_data = util.read_all_lines(file_name)
    pass


@util.time_it_and_evaluate
def solve_1(data):
    pass


@util.time_it_and_evaluate
def solve_2(data):
    pass


if __name__ == '__main__':
    input = parse_input_data('../data/day0/input_example.txt')
    # input = parse_input_data('../data/day0/input.txt')
    solve_1(input)
    solve_2(input)
