import re

red_count = 12
green_count = 13
blue_count = 14

def is_possible(game_line: str):
    game_id, game_record = game_line.split(": ")
    game_id = int(re.findall(r'\d+', game_id)[0])
    game_record = game_record.split("; ")
    for record in game_record:
        colors = record.split(", ")
        for color in colors:
            num, name = color.split(" ")
            if name == "red" and int(num) > red_count:
                return (False, game_id)
            elif name == "green" and int(num) > green_count:
                return (False, game_id)
            elif name == "blue" and int(num) > blue_count:
                return (False, game_id)
    return (True, game_id)


if __name__ == '__main__':
    sum = 0
    with open("2023/Day 2/input.txt") as file:
        for line in file.read().split('\n'):
            b, n = is_possible(line)
            if b:
                sum += n
    print(sum)
