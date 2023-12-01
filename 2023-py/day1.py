with open('data/1-1.txt', 'r') as file:
    data = [m.strip() for m in file.readlines()]


def one():
    sm = 0
    for line in data:
        digits = [char for char in line if char.isdigit()]
        sm += int(digits[0] + digits[-1])
    return sm


def two():
    lut = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    sm = 0
    for line in data:
        digits = []
        line_len = len(line)

        for i in range(line_len):
            if line[i].isdigit():
                digits.append(line[i])

            elif i + 3 <= line_len and line[i:i + 3] in lut:
                digits.append(lut[line[i:i + 3]])

            elif i + 4 <= line_len and line[i:i + 4] in lut:
                digits.append(lut[line[i:i + 4]])

            elif i + 5 <= line_len and line[i:i + 5] in lut:
                digits.append(lut[line[i:i + 5]])

        sm += int(digits[0] + digits[-1])
    return sm


if __name__ == '__main__':
    print(two())
