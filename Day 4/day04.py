import sys
import re
from collections import defaultdict 

data = open(sys.argv[1]).read().strip() 

lines = data.split('\n')
total = 0
reps = defaultdict(int)

for i, line in enumerate(lines):
    reps[i] += 1
    card, nums = line.split(':')
    first, second = nums.split('|')
    winning = [int(x) for x in first.split()]
    draws = [int(x) for x in second.split()]
    wins = len(set(winning) & set(draws)) 

    for j in range(wins):
        reps[i+j+1] += reps[i]

    if wins > 0:
        total += 2 ** (wins - 1)
    
print(total)
print(sum(reps.values()))

