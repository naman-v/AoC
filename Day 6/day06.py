import sys
import re
from collections import defaultdict 

data = open(sys.argv[1]).read().strip() 

lines = data.split('\n')
times = lines[0].split()[1:]
records = lines[1].split()[1:]

raceTime = int("".join(times))
record = int("".join(records))


counter = 0

for holdTime in range(raceTime):
    distance = (raceTime - holdTime) * holdTime   
    if distance > record:
        counter += 1

print(counter)