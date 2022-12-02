from collections import deque
from functools import reduce

import util


def parse_input_data(file_name):
    read_data = util.read_all_lines(file_name)
    return read_data


def peek(queue):
    if queue:
        return queue[-1]


"""
removes pairs as it reads them

{([(<{}[<>[]}>{[]{[(<()>
     ^^
{([(<[<>[]}>{[]{[(<()>
      ^^
{([(<[[]}>{[]{[(<()>
      ^^
{([(<[}>{[]{[(<()>
     ^^ <= error


[({(<(())[]>[[{[]{<()<>>
      ^^
[({(<()[]>[[{[]{<()<>>
     ^^
[({(<[]>[[{[]{<()<>>
     ^^
[({(<>[[{[]{<()<>>
    ^^
[({([[{[]{<()<>>
       ^^
[({([[{{<()<>>
         ^^
[({([[{{<<>>
         ^^
[({([[{{<>
        ^^
[({([[{{
        ^ <= clean / also remainder is all the missing part. useful in part 2
"""


def find_error(line):
    stack = deque()
    for c in line:
        if stack and c in pairs.keys():
            if peek(stack) == pairs[c]:
                stack.pop()
                continue
            else:
                return c
        stack.append(c)
    return ''


@util.time_it_and_evaluate
def solve_1(data):
    score_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    clean_lins = [find_error(line) for line in data]
    return sum(map(lambda c: score_map[c], filter(lambda e: e, clean_lins)))


def get_autocomplete_symbols(line):
    stack = deque()
    for c in line:
        if stack and c in pairs.keys():
            if peek(stack) == pairs[c]:
                stack.pop()
                continue
        stack.append(c)
    stack.reverse()
    return [pairs_rev[c] for c in stack if c in pairs_rev]


def calculate_score(chars):
    score_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    return reduce(lambda a, e: a * 5 + e, map(lambda e: score_map[e], chars))


@util.time_it_and_evaluate
def solve_2(data):
    completed_chars = []
    for line in data:
        c = find_error(line)
        if not c:
            completed_chars.append(calculate_score(get_autocomplete_symbols(line)))
    return sorted(completed_chars)[len(completed_chars) // 2]


if __name__ == '__main__':
    # input = parse_input_data('../data/day10/input_example.txt')
    input = parse_input_data('../data/day10/input.txt')

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }

    pairs_rev = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    solve_1(input)
    solve_2(input)
