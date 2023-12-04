def check_prize(win, our):
    prize = 0
    for num in win:
        if num in our:
            prize = 1 if prize == 0 else prize*2
    return prize


if __name__ == '__main__':
    sum = 0
    with open("Day 4/input.txt") as file:
        for line in file.read().split('\n'):
            game, nums = line.split(': ')
            win, our = [x.split(' ') for x in nums.split(' | ')]
            while('' in win): win.remove('')
            while('' in our): our.remove('')
            win = [int(x) for x in win]
            our = [int(x) for x in our]
            sum += check_prize(win, our)
    print(sum)