if __name__ == '__main__':
    floor = 0
    with open("2015/Day 1/input.txt") as file:
        for line in file:
            for char in line:
                floor = floor + 1 if char == '(' else floor - 1
    print(floor)