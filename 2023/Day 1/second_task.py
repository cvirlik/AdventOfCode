import regex as re

num_str = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def convert_to_num(str_num: str, mul: int):
    if str_num.isdigit():
        return int(str_num) * mul
    else:
        return num_str[str_num] * mul


def get_num(text_line: str):
    numbers_pattern = r'\d|one|two|three|four|five|six|seven|eight|nine'

    regex_result = re.findall(numbers_pattern, text_line, overlapped=True)
    return convert_to_num(regex_result[0], 10) + convert_to_num(regex_result[-1], 1)


if __name__ == '__main__':
    sum = 0
    with open("2023/Day 1/input.txt") as file:
        for line in file:
            sum += get_num(line)
    print(sum)
