import util

def read_input(filename: str) -> tuple[list, list]:
    random_digits: list = []
    bingos: list = []
    with open(filename, 'r') as input_file:
        read_data = input_file.read().split("\n\n")
    random_digits.extend(map(lambda num: int(num), read_data[0].split(",")))

    for bingo in read_data[1:]:
        parsed_bingo = []
        for row in bingo.split("\n"):
            parsed_row = []
            for cell in row.split(" "):
                if cell:
                    parsed_row.append(int(cell))
            parsed_bingo.append(parsed_row)
        bingos.append(parsed_bingo)

    return random_digits, bingos


def is_winner(bingo):
    iterators = []
    iterators.extend(row for row in bingo)
    iterators.extend([[row[i] for row in bingo] for i in range(5)])
    filter_visited = [[cell for cell in row if cell < 0] for row in iterators]
    return len([row for row in filter_visited if len(row) == 5]) > 0


def mark_digit(digit, bingo):
    for i, row in enumerate(bingo):
        for j, cell in enumerate(row):
            if cell == digit:
                bingo[i][j] += 1
                bingo[i][j] *= -1
                return


def unmarked_digits(bingo):
    for i, row in enumerate(bingo):
        for j, cell in enumerate(row):
            if cell > 0:
                yield bingo[i][j]

@util.time_it_and_evaluate
def solve_1(digits, bingos):
    for digit in digits:
        for bingo in bingos:
            mark_digit(digit, bingo)
            if is_winner(bingo):
                sm = sum(unmarked_digits(bingo))
                d = digit
                return sm * d

@util.time_it_and_evaluate
def solve_2(digits, bingos):
    for digit in digits:
        i = 0
        while i < len(bingos):
            bingo = bingos[i]
            mark_digit(digit, bingo)
            if is_winner(bingo):
                if len(bingos) == 1:
                    sm = sum(unmarked_digits(bingo))
                    d = digit
                    return sm * d
                bingos.remove(bingo)
                i -= 1
            i += 1


if __name__ == '__main__':
    digits, bingos = read_input('../data/day4/input.txt')
    solve_1(digits, bingos)
    solve_2(digits, bingos)
