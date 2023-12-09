import sys
import re
from collections import defaultdict 

data = open(sys.argv[1]).read().strip() 

lines = data.split('\n')
times = lines[0].split()[1:]
records = lines[1].split()[1:]

possibleWins = [] * len(times)

res = 1

raceTime = 0
record = 0

for i in range(len(times)):
    raceTime = int(times[i])
    record = int(records[i])

    counter = 0
    for holdTime in range(raceTime):
        distance = (raceTime - holdTime) * holdTime   
        if distance > record:
            counter += 1
    possibleWins.append(counter)

for win in possibleWins:
    res *= win 

print(res)