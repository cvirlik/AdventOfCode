import re


def get_num(text_line: str):
    return (int(re.search(r'\d+', text_line).group()[0]) * 10 +
            int(re.search(r'\d+', text_line[::-1]).group()[0]))


if __name__ == '__main__':
    sum = 0
    with open("2023/Day 1/input.txt") as file:
        for line in file:
            sum += get_num(line)
    print(sum)
