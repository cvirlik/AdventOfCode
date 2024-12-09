import copy
def read_file(file_name):
    with open(file_name, 'r') as data:
        content = data.read()
        lines = content.split("\n")
        matrix = [list(x) for x in lines]
        return matrix

def find_start(matrix):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == "^":
                return (i, j)
    return None

def calculate_steps(matrix):
    sum = 0
    for row in matrix: 
        sum += row.count("X")
    return sum

def step_forward(matrix, starting, direction):
    x, y = starting
    directions = {
        "up": (-1, 0, "right"),
        "down": (1, 0, "left"),
        "left": (0, -1, "up"),
        "right": (0, 1, "down")
    }

    while True:
        dx, dy, next_dir = directions[direction]
        nx, ny = x + dx, y + dy

        if nx < 0 or ny < 0 or nx >= len(matrix) or ny >= len(matrix[0]):
            matrix[x][y] = "X"
            break

        if matrix[nx][ny] == "#": 
            direction = next_dir  
        else:  
            matrix[x][y] = "X" 
            x, y = nx, ny

def first_task(map, start, direction):
    step_forward(map, start, direction)
    print(calculate_steps(map))

def step_forward_modified(matrix, starting, direction):
    x, y = starting
    recorded_steps = [[None for _ in row] for row in matrix]
    directions = {
        "up": (-1, 0, "right"),
        "down": (1, 0, "left"),
        "left": (0, -1, "up"),
        "right": (0, 1, "down")
    }

    while True:
        dx, dy, next_dir = directions[direction]
        nx, ny = x + dx, y + dy
        
        if matrix[x][y] == "X" and recorded_steps[x][y] == direction:
            return True

        if nx < 0 or ny < 0 or nx >= len(matrix) or ny >= len(matrix[0]):
            matrix[x][y] = "X"
            return False

        if matrix[nx][ny] == "#": 
            direction = next_dir  
        else:  
            matrix[x][y] = "X" 
            recorded_steps[x][y] = direction
            x, y = nx, ny

def second_task(map, start, direction):
    cycles = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "^":
                continue
            if map[i][j] == ".":
                temp = copy.deepcopy(map)
                temp[i][j] = "#"
                if step_forward_modified(temp, start, direction):
                    cycles += 1
    print(cycles)


if __name__ == '__main__':
    map = read_file("Day 6/input.txt")
    start = find_start(map)
    direction = "up"
    first_task(copy.deepcopy(map), start, direction)
    second_task(copy.deepcopy(map), start, direction)
    