import numpy as np 
import itertools

def unique_combinations(elements: list[str]) -> list[tuple[str, str]]:
    return list(itertools.combinations(elements, 2))

if __name__ == '__main__':
    matrix = []
    with open("2023/Day 11/input.txt") as file:
        for line in file.read().split('\n'):
            matrix.append([*line])
    matrix = np.array(matrix)

    idxr = []
    offset = 0
    for i in range(len(matrix)):
        if not '#' in matrix[i]:
            idxr.append(i + offset)
            offset += 1
    for i in idxr:
        matrix = np.insert(matrix, i+1, matrix[i], 0) 

    idxc = []
    offset = 0
    for j in range(len(matrix[0])):
        copy = True
        for i in range(len(matrix)):
            if matrix[i][j] == '#':
                copy = False
                break
        if copy:
            idxc.append(j + offset)
            offset += 1
    for j in idxc:
        matrix = np.insert(matrix, j+1, matrix[:, j], 1) 

    galaxies = list(zip(*np.where(matrix == '#')))
    galaxies = unique_combinations(galaxies)

    dist = 0
    for pair in galaxies:
        dist += max(pair[0][0], pair[1][0]) - min(pair[0][0], pair[1][0]) + max(pair[0][1], pair[1][1]) - min(pair[0][1], pair[1][1])
    print(dist)


                  