import re


def find_wins(game):
    time, distance = game[0], game[1]
    v = -1
    wins = 0
    for t in range(0, time+1):
        v += 1
        current_distance = v * (time - t)
        if current_distance > distance:
            wins += 1
    return wins



if __name__ == '__main__':
    with open("2023/Day 6/input.txt") as file:
        time, distance = file.readlines()
        time = list(map(int, re.findall(r'\d+', time)))
        distance = list(map(int, re.findall(r'\d+', distance)))
        games = [(x, y) for x, y in zip(time, distance)]
        win = 1
        for game in games:
            win *= find_wins(game)
    print(win)

