def extrapolation(diff):
    exp = 0
    for item in diff[::-1]:
        exp = item[0] - exp
    return exp


if __name__ == '__main__':
    predict_sum = 0
    with open("2023/Day 9/input.txt") as file:
        for line in file.read().split('\n'):
            diff = []
            diff.append(list(map(int, line.split(' '))))
            while not all(v == 0 for v in diff[-1]):
               diff.append([diff[-1][i+1]-diff[-1][i] for i in range(len(diff[-1])-1)])
            predict_sum += extrapolation(diff)
    print(predict_sum)
