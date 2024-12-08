def read_file(file_name):
    with open(file_name, 'r') as data:
        x = []
        y = []
        for line in data:
            left, right = line.split()
            x.append(int(left))
            y.append(int(right))

    return x, y

def first_task(left, right):
    print(sum([abs(x - y) for x, y in zip(left, right)]))

def second_task(left, right):
    sum = 0
    for element in left:
        sum += element * right.count(element)
    print(sum)



if __name__ == '__main__':
    left, right = read_file("Day 1/input.txt")
    left.sort()
    right.sort()

    first_task(left, right)
    second_task(left, right)
    