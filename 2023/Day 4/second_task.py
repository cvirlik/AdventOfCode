import re


def check_prize(win, our, card: int, cards: dict):
    prize_amount = 0
    for num in win:
        if num in our:
            prize_amount += 1
    for i in range(card+1, card+1+prize_amount):
        cards[i] += cards[card]


if __name__ == '__main__':
    cards = {}
    with open("2023/Day 4/input.txt") as file:
        x = len(file.readlines())
        for i in range(x):
            cards[i+1] = 1

    with open("2023/Day 4/input.txt") as file:
        for line in file.read().split('\n'):
            card, nums = line.split(': ')
            card = int(re.search(r'\d+', card).group())
            win, our = [x.split(' ') for x in nums.split(' | ')]
            while('' in win): win.remove('')
            while('' in our): our.remove('')
            win = [int(x) for x in win]
            our = [int(x) for x in our]
            check_prize(win, our, card, cards)
    print(sum(cards.values()))