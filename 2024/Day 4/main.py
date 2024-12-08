import re
import numpy as np
def read_file(file_name):
    with open(file_name, 'r') as data:
        content = data.read()
        return content.split('\n')


def first_task(wordsearch):
    xmas = 0
    matrix = []
    for line in wordsearch:
        xmas += len(re.findall(r"XMAS", line))
        xmas += len(re.findall(r"SAMX", line))
        matrix.append(list(line))
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for line in transpose:
        column = "".join(str(x) for x in line)
        xmas += len(re.findall(r"XMAS", column))
        xmas += len(re.findall(r"SAMX", column))
    matrix = np.array(matrix)
    diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1])]
    diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1))

    diags = [n.tolist() for n in diags]

    for diag in diags:
        column = "".join(str(x) for x in diag)
        xmas += len(re.findall(r"XMAS", column))
        xmas += len(re.findall(r"SAMX", column))

    print(xmas)

def second_task(wordsearch):
    xmas = 0
    matrix = []
    for line in wordsearch:
        matrix.append(list(line))
    for i in range(1, len(matrix)-1):
        for j in range(1, len(line)-1):
            if matrix[i][j] == "A":
                if (matrix[i-1][j-1] == "S" and matrix[i+1][j+1] == "M") or (matrix[i-1][j-1] == "M" and matrix[i+1][j+1] == "S"):
                    if (matrix[i-1][j+1] == "S" and matrix[i+1][j-1] == "M") or (matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S"): 
                        xmas += 1
    print(xmas)


if __name__ == '__main__':
    wordsearch= read_file("Day 4/input.txt")
    first_task(wordsearch)
    second_task(wordsearch)
    