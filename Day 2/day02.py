import re

with open('input.txt', 'r') as file:
    lines = file.readlines() 

dict = {"red": 12, "green": 13, "blue": 14}

res = 0
power = 0

for line in lines:
    spl = line.split(":")
    game = int(spl[0].split()[1])
    sets = spl[1].split(";")
    possible = True

    max = {"red": 0, "green": 0, "blue": 0}
    for set in sets:
        pulls = set.split(",")
        
        for pull in pulls:
            num, color = int(pull.split()[0]), pull.split()[1]

            if dict[color] < num:
                possible = False 
            if max[color] < num:
                max[color] = num

    product = 1
    for value in max.values():
        product *= value
    power += product

    if possible:
        res += game 

print(res)
print(power)