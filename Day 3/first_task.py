import re

def check_index(i, j):
    return matrix[i][j] != '.' and not matrix[i][j].isdigit()

def check_collision(matrix, i, j):
    # UP
    if i != 0:
        if check_index(i - 1, j):
            return True
        # LEFT DIAGONAL
        if j != 0:
            if check_index(i - 1, j - 1):
                return True
        # RIGHT DIAGONAL
        if j != len(matrix[i])-1:
            if check_index(i - 1, j + 1):
                return True
    # DOWN 
    if i != len(matrix)-1:
        if check_index(i + 1, j):
            return True
        # LEFT DIAGONAL
        if j != 0:
            if check_index(i + 1, j - 1):
                return True
        # RIGHT DIAGONAL
        if j != len(matrix[i])-1:
            if check_index(i + 1, j + 1):
                return True
    # LEFT
    if j != 0:
            if check_index(i, j - 1):
                return True
    # RIGHT
    if j != len(matrix[i])-1:
            if check_index(i, j + 1):
                return True
    return False

def find_parts(matrix):
    sum = 0
    digit = ''
    is_valid = False
    for r in range(len(matrix)):
        for i in range(len(matrix[0])):
            if matrix[r][i].isdigit():
                digit = digit + matrix[r][i]
                if not is_valid:
                    is_valid = check_collision(matrix, r, i)
            else:
                if not digit:
                    continue
                elif is_valid:
                    sum += int(digit)
                is_valid = False
                digit = ''
    return sum


if __name__ == '__main__':
    sum = 0
    matrix = []
    with open("Day 3/input.txt") as file:
        for line in file.read().split('\n'):
            matrix.append(re.findall(r'\S', line))
    print(find_parts(matrix))