from collections import Counter


def card_sort(t):
    order = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, 
             '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}
    return [order[c] for c in t[0]] 


def sort_hands(hands: dict):
    for key in hands.keys():
        hands[key] = sorted(hands[key], key=card_sort)  
    return hands


def count_win(sorded_hands):
    win = 0
    rank = len(sorded_hands)
    for hand in sorded_hands:
        win += int(hand[1]) * rank
        rank -= 1
    return win


if __name__ == '__main__':
    hands = {
        (5,) : [],
        (4, 1) : [],
        (3, 2) : [],
        (3, 1, 1) : [],
        (2, 2, 1) : [],
        (2, 1, 1, 1) : [],
        (1, 1, 1, 1, 1) : []
    }
    with open("2023/Day 7/input.txt") as file:
        for line in file.read().split('\n'):
            hand, bid = line.split(' ')
            WC = Counter(hand)
            hands[tuple(sorted(tuple(WC.values()), reverse=True))].append((hand, bid))
    
    sorded_hands = list(sort_hands(hands).values())
    sorded_hands = [item for sublist in sorded_hands for item in sublist]
    print(count_win(sorded_hands))
