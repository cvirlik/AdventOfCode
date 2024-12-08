def roll_out(matrix):
    for i in range(len(matrix)):
        if i == 0:
            continue
        for j in range(len(matrix)):
            if matrix[i][j] == 'O':
                k = i
                while k != 0 and matrix[k - 1][j] == '.':
                    matrix[k-1][j] = 'O'
                    matrix[k][j] = '.'
                    k -= 1


if __name__ == '__main__':
    matrix = []
    with open("2023/Day 14/input.txt") as file:
        for line in file.read().split('\n'):
            matrix.append([*line])
    sum = 0
    roll_out(matrix)
    for i in range(len(matrix)):
        sum += matrix[i].count('O') * (len(matrix) - i)
    print(sum)