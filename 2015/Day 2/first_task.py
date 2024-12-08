def find_meters(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + min(l*w , w*h , h*l)


if __name__ == '__main__':
    sum = 0
    with open("2015/Day 2/input.txt") as file:
        for line in file.read().split('\n'):
            l, w, h = [int(x) for x in line.split('x')]
            sum += find_meters(l, w, h)
    print(sum)