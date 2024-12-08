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
        time = int(''.join(re.findall(r'\d+', time)))
        distance =  int(''.join(re.findall(r'\d+', distance)))
        win = find_wins((time, distance))
    print(win)

