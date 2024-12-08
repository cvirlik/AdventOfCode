def find_meters(l, w, h):
    a = [l, w, h]
    a.remove(max(l, w, h))
    return l*w*h + a[0]*2+a[1]*2


if __name__ == '__main__':
    sum = 0
    with open("2015/Day 2/input.txt") as file:
        for line in file.read().split('\n'):
            l, w, h = [int(x) for x in line.split('x')]
            sum += find_meters(l, w, h)
    print(sum)