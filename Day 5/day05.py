import sys
import re
from collections import defaultdict 

def createMaps(category, values):
    dest = int(values[0])
    source = int(values[1])
    r = int(values[2])
    
    maps[category][source] = (source, source + r - 1, dest, dest + r - 1)

def getMapping(category, value):
    if value in maps[category]:
        return maps[category][value][2]

    for bound,bound_val in maps[category].items():
        if bound_val[0] < value <= bound_val[1]:
            return bound_val[2] + value - bound_val[0]
    return value

####### HELPER FUNCTIONS ABOVE #########

data = open(sys.argv[1]).read().strip() 

lines = data.split('\n') 
temp = lines[0].split(':')[1]
seeds = [int(x) for x in temp.split()]

locations = []
maps = {"seed": {}, "soil": {}, "fertilizer": {}, "water": {}, "light": {}, "temperature": {}, "humidity": {}}
curr = " "

for line in lines[2:]:
    mapping = line.split('-')[0]
    
    if mapping in maps:
        curr = mapping
        continue

    if len(mapping) > 0:
        values = mapping.split(' ')
        createMaps(curr, values) 


for i in range(100):
    value = i
    for key in maps.keys():
        value = getMapping(key, value)
    print(i,value)
    locations.append(value)

print(min(locations))
# print(min(locations)) #part 1
#######################################

