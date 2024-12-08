def find_destination(dir: str, graph: dict, start_point: str):
    current_point = start_point
    lenght = 0
    i = 0
    while current_point != 'ZZZ':
        if i == len(dir):
            i = 0
        turn = dir[i]
        current_point = graph[current_point][0] if turn == 'L' else graph[current_point][1]
        i += 1
        lenght += 1
    return lenght


if __name__ == '__main__':
    dir = ''
    graph = {}
    start = 'AAA'
    with open("2023/Day 8/input.txt") as file:
        dir = file.readline().replace('\n', '')
        for line in file.read().split('\n'):
            if line == '':
                continue
            d, lr = line.split(' = ')
            lr = lr.replace('(', '')
            lr = lr.replace(')', '')
            lr = tuple(lr.split(', '))
            graph[d] = lr
    print(find_destination(dir, graph, start))
    
