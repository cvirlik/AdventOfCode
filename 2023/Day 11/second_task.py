import numpy as np 
import itertools

def unique_combinations(elements: list[str]) -> list[tuple[str, str]]:
    return list(itertools.combinations(elements, 2))

if __name__ == '__main__':
    matrix = []
    offset = 1000000-1
    with open("2023/Day 11/input.txt") as file:
        for line in file.read().split('\n'):
            matrix.append([*line])
    matrix = np.array(matrix)

    idxr = [0]*len(matrix)
    for i in range(len(matrix)):
        if not '#' in matrix[i]:
            print(i)
            idxr[i:] = [x + offset for x in idxr[i:]]
    print(idxr)

    idxc = [0]*len(matrix[0])
    for j in range(len(matrix[0])):
        copy = True
        for i in range(len(matrix)):
            if matrix[i][j] == '#':
                copy = False
                break
        if copy:
            idxc[j:] = [x + offset for x in idxc[j:]]
    print(idxc)

    galaxies = list(zip(*np.where(matrix == '#')))
    galaxies = unique_combinations(galaxies)

    dist = 0
    for pair in galaxies:
        x1, x2 = pair[0][0], pair[1][0]
        x1 = x1 + idxr[x1]
        x2 = x2 + idxr[x2]

        y1, y2 = pair[0][1], pair[1][1]
        y1 = y1 + idxc[y1]
        y2 = y2 + idxc[y2]

        dist += max(x1, x2) - min(x1, x2) + max(y1, y2) - min(y1, y2)
    print(dist)
