import re


def is_possible(game_line: str):
    game_id, game_record = game_line.split(": ")
    game_id = int(re.findall(r'\d+', game_id)[0])
    game_record = game_record.split("; ")
    r, g, b = -1, -1, -1
    for record in game_record:
        colors = record.split(", ")
        for color in colors:
            num, name = color.split(" ")
            num = int(num)
            if name == "red":
                r = max(num, r)
            elif name == "green":
                g = max(num, g)
            elif name == "blue":
                b = max(num, b)
    return (r, g, b)


if __name__ == '__main__':
    sum = 0
    with open("2023/Day 2/input.txt") as file:
        for line in file.read().split('\n'):
            r, g, b = is_possible(line)
            if b:
                sum += r*g*b
    print(sum)
