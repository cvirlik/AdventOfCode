import re

def check_index(i, j, gear):
    if matrix[i][j] == "*":
        gear.append((i, j))

def check_collision(matrix, i, j):
    gear = []
    # UP
    if i != 0:
        check_index(i - 1, j, gear)
        # LEFT DIAGONAL
        if j != 0:
            check_index(i - 1, j - 1, gear)
        # RIGHT DIAGONAL
        if j != len(matrix[i])-1:
            check_index(i - 1, j + 1, gear)
    # DOWN 
    if i != len(matrix)-1:
        check_index(i + 1, j, gear)
        # LEFT DIAGONAL
        if j != 0:
            check_index(i + 1, j - 1, gear)
        # RIGHT DIAGONAL
        if j != len(matrix[i])-1:
            check_index(i + 1, j + 1, gear)
    # LEFT
    if j != 0:
        check_index(i, j - 1, gear)
    # RIGHT
    if j != len(matrix[i])-1:
        check_index(i, j + 1, gear)
    return gear

def find_parts(matrix):
    sum = 0
    digit = ''
    num = {}
    gear = []
    for r in range(len(matrix)):
        for i in range(len(matrix[0])):
            if matrix[r][i].isdigit():
                digit = digit + matrix[r][i]
                gear += check_collision(matrix, r, i)
            else:
                if not digit:
                    continue
                elif gear:
                    gear = list(dict(gear).items())
                    for key in gear:
                        if key not in num:
                            num[key] = [int(digit)]
                        else:
                            num[key].append(int(digit))
                gear = []
                digit = ''
    for k in num.keys():
        if len(num[k]) == 2:
            sum += num[k][0] * num[k][1]
    return sum


if __name__ == '__main__':
    sum = 0
    matrix = []
    with open("Day 3/input.txt") as file:
        for line in file.read().split('\n'):
            matrix.append(re.findall(r'\S', line))
    print(find_parts(matrix))