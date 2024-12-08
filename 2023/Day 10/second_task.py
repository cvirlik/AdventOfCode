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
    loop = []
    # TOP
    if x != 0 and is_valid(matrix[x][y], matrix[x-1][y], 't', [], 0, 0):
        vis = [start]
        define_steps(x-1, y, 0, vis)
        loop = vis if len(vis) > len(loop) else loop

    # BOTTOM
    if x != len(matrix)-1 and is_valid(matrix[x][y], matrix[x+1][y], 'b', [], 0, 0):
        vis = [start]
        define_steps(x+1, y, 0, vis)
        loop = vis if len(vis) > len(loop) else loop
    
    # LEFT
    if y != 0 and is_valid(matrix[x][y], matrix[x][y-1], 'l', [], 0, 0):
        vis = [start]
        define_steps(x, y-1, 0, vis)
        loop = vis if len(vis) > len(loop) else loop

    # RIGHT
    if y != len(matrix[0])-1 and is_valid(matrix[x][y], matrix[x][y+1], 'r', [], 0, 0):
        vis = [start]
        define_steps(x, y+1, 0, vis)
        loop = vis if len(vis) > len(loop) else loop
    return loop


def index2d(list2d, value):
    return next((i, j) for i, lst in enumerate(list2d)
                for j, x in enumerate(lst) if x == value)


def is_point_in_path(x: int, y: int, poly) -> bool:
    """Determine if the point is on the path, corner, or boundary of the polygon

    Args:
      x -- The x coordinates of point.
      y -- The y coordinates of point.
      poly -- a list of tuples [(x, y), (x, y), ...]

    Returns:
      True if the point is in the path or is a corner or on the boundary"""
    num = len(poly)
    j = num - 1
    c = False
    for i in range(num):
        if (x == poly[i][0]) and (y == poly[i][1]):
            # point is a corner
            return False
        if (poly[i][1] > y) != (poly[j][1] > y):
            slope = (x - poly[i][0]) * (poly[j][1] - poly[i][1]) - (
                poly[j][0] - poly[i][0]
            ) * (y - poly[i][1])
            if slope == 0:
                # point is on boundary
                return False
            if (slope < 0) != (poly[j][1] < poly[i][1]):
                c = not c
        j = i
    return c


if __name__ == '__main__':
    with open("2023/Day 10/input.txt") as file:
        for line in file.read().split('\n'):
            matrix.append([*line])
    start = index2d(matrix, 'S')
    steps = [[0]*len(matrix[0]) for i in range(len(matrix))]
    pipes = [['0']*len(matrix[0]) for i in range(len(matrix))]
 
    loop = init_start(start[0], start[1], -1)
    for item in loop:
        pipes[item[0]][item[1]] = '1'

    for i in range(len(pipes)):
        for j in range(len(pipes[0])):
            if is_point_in_path(i, j, loop):
                pipes[i][j] = '*'

    print(sum(row.count('*') for row in pipes))



