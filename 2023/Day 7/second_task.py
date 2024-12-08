from collections import Counter
import operator


def card_sort(t):
    order = {'A': 0, 'K': 1, 'Q': 2, 'T': 3, 
             '9': 4, '8': 5, '7': 6, '6': 7, '5': 8, '4': 9, '3': 10, '2': 11, 'J': 12}
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
            if 'J' in WC.keys() and len(WC.keys()) != 1:
                delta = WC['J']
                del WC['J']
                WC[max(WC.items(), key=operator.itemgetter(1))[0]] += delta
            hands[tuple(sorted(tuple(WC.values()), reverse=True))].append((hand, bid))
    
    sorded_hands = list(sort_hands(hands).values())
    sorded_hands = [item for sublist in sorded_hands for item in sublist]
    print(count_win(sorded_hands))
