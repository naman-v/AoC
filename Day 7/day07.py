import re
import sys
from collections import defaultdict, Counter
from functools import cmp_to_key

def getRank(numUnique, handValues):
    handRank = 1
    if numUnique == 1:
        handRank = 7                # five of kind
    elif numUnique == 2:
        if 4 == handValues:
            handRank = 6            # four of a kind
        else:
            handRank = 5            # full house
    elif numUnique == 3:
        if 3 == handValues:
            handRank = 4            # thee of a kind
        else:
            handRank = 3            # two pair
    else:
        handRank = 6 - numUnique    # One pair and High Card
    
    return handRank


data = open(sys.argv[1]).read().strip() 
lines= data.split('\n')

vals = {'T':10, 'J': 11, 'Q': 12, 'K':13, 'A': 14}
aggregate = []

for line in lines: 
    cards, bid = line.split()

    hand = {}
    enum = 0
    for card in cards:
        hand[card] = hand.get(card,0) + 1
        if card in vals:
            enum = enum*10 + vals[card]
        else:
            enum = enum*10 + int(card)

    # print(max(Counter(cards).values()))

    handRank = getRank(len(hand), max(hand.values()))
    enum = handRank * (10**5) + enum 

    aggregate.append((enum,int(bid)))
    
sorted = sorted(aggregate, key = lambda x: x[0])

winnings = 0

for i, hand in enumerate(sorted):
    winnings += (i + 1) * hand[1]

print(winnings)
    