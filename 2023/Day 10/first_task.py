import sys
from collections import deque

connections = {
    'S': {'l': ['-', 'L', 'F'],
          'r': ['-', 'J', '7'],
          't': ['|', '7', 'F'],
          'b': ['|', 'L', 'J']},

    '|': {'l': [],
          'r': [],
          't': ['|', '7', 'F'],
          'b': ['|', 'L', 'J']},

    '-': {'l': ['-', 'L', 'F'],
          'r': ['-', 'J', '7'],
          't': [],
          'b': []},

    'L': {'l': [],
          'r': ['-', 'J', '7'],
          't': ['|', '7', 'F'],
          'b': []},

    'J': {'l': ['-', 'L', 'F'],
          'r': [],
          't': ['|', '7', 'F'],
          'b': []},

    '7': {'l': ['-', 'F', 'L'],
          'r': [],
          't': [],
          'b': ['|', 'L', 'J']},

    'F': {'l': [],
          'r': ['J', '-', '7'],
          't': [],
          'b': ['|', 'L', 'J']}
}

matrix = []
steps = []
start = ()

def is_valid(st: str, cn: str, dist: str, vis, x, y):
    return cn in connections[st][dist] and (x, y) not in vis


def define_steps(x, y, l, vis):
    queue = deque([(x, y, l)])
    vis = []
    while queue:
        x, y, l = queue.popleft()
        if steps[x][y] == 0 or steps[x][y] > l + 1:
            steps[x][y] = l + 1 
            vis.append((x, y))
            # TOP
            if x != 0 and is_valid(matrix[x][y], matrix[x-1][y], 't', vis, x-1, y):
                queue.append((x-1, y, steps[x][y]))
            # BOTTOM
            if x != len(matrix)-1 and is_valid(matrix[x][y], matrix[x+1][y], 'b', vis, x+1, y):
                queue.append((x+1, y, steps[x][y]))
            # LEFT
            if y != 0 and is_valid(matrix[x][y], matrix[x][y-1], 'l', vis, x, y-1):
                queue.append((x, y-1, steps[x][y]))
            # RIGHT
            if y != len(matrix[0])-1 and is_valid(matrix[x][y], matrix[x][y+1], 'r', vis, x, y+1):
                queue.append((x, y+1, steps[x][y]))


def init_start(x, y, l):
    steps[x][y]= 0
    # TOP
    if x != 0 and is_valid(matrix[x][y], matrix[x-1][y], 't', [], 0, 0):
        define_steps(x-1, y, 0, [])

    # BOTTOM
    if x != len(matrix)-1 and is_valid(matrix[x][y], matrix[x+1][y], 'b', [], 0, 0):
        define_steps(x+1, y, 0, [])
    
    # LEFT
    if y != 0 and is_valid(matrix[x][y], matrix[x][y-1], 'l', [], 0, 0):
        define_steps(x, y-1, 0, [])

    # RIGHT
    if y != len(matrix[0])-1 and is_valid(matrix[x][y], matrix[x][y+1], 'r', [], 0, 0):
        define_steps(x, y+1, 0, [])


def index2d(list2d, value):
    return next((i, j) for i, lst in enumerate(list2d)
                for j, x in enumerate(lst) if x == value)


if __name__ == '__main__':
    with open("2023/Day 10/input.txt") as file:
        for line in file.read().split('\n'):
            matrix.append([*line])
    start= index2d(matrix, 'S')
    steps= [[0]*len(matrix[0]) for i in range(len(matrix))]

    init_start(start[0], start[1], -1)

    maximum= -1
    for item in steps:
        for i in item:
            maximum= max(i, maximum)
    print(maximum)
