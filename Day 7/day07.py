import re
import sys
import collections  
from functools import cmp_to_key

def rankEval(x, y):
    
    for i in range(len(x)):
        a = vals[x[i]] if x[i] in vals else int(x[i])
        b = vals[y[i]] if y[i] in vals else int(y[i])

        # vals.get(x[i], int(x[i]))          idk why this doesnt work fml
        # b = vals.get(y[i], int(y[i])
        if a > b:
            return x
        elif b > a:
            return y

    return x


data = open(sys.argv[1]).read().strip() 
lines= data.split('\n')

vals = {'T':10, 'J': 11, 'Q': 12, 'K':13, 'A': 14}
aggregate = []

bids = []

for line in lines: 
    cards, bid = line.split()
    bids.append(bid)

    hand = {}

    for card in cards:
        hand[card] = hand.get(card,0) + 1

    numUnique = len(hand)
    if numUnique == 1:
        handRank = 7                # five of kind
    elif numUnique == 2:
        if 4 in hand.values():
            handRank = 6            # four of a kind
        else:
            handRank = 5            # full house
    elif numUnique == 3:
        if 3 in hand.values():
            handRank = 4            # thee of a kind
        else:
            handRank = 3            # two pair
    else:
        handRank = 6 - numUnique    # One pair and High Card
    
    aggregate.append(str(handRank) + cards)
 
ranks = sorted(aggregate, key = lambda x: (rankEval(aggregate[0], aggregate[1])))
 
print(aggregate)

    
    