import string

with open('input.txt', 'r') as data:
    file = data.readlines()

sum = 0
total = 0

directions = [[0,1], [1,0], [-1,0], [0,-1], [1,1], [-1,1], [1,-1], [-1,-1]]
symbols = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '/', '+', '-', '=' }
rows = len(file)
cols = len(file[0])
skip_iterations = 0

gear = {}

for row in range (rows):
    for col in range(cols):

        if skip_iterations > 0:
            skip_iterations -= 1
            continue

        num = 0
        isPartNum = False
        isGear = False
        gearLocation = 0

        while file[row][col].isdigit():
            num = 10*num + int(file[row][col])

            if not isPartNum:
                for dir in directions:
                    x,y = row + dir[0], col + dir[1]
                    if x >= 0 and x < rows and y >= 0 and y < cols:
                        if file[x][y] in symbols:
                            isPartNum = True 

                        if file[x][y] == '*':
                            isGear = True
                            gearLocation = (x,y)

            skip_iterations += 1
            col += 1
        
        if isPartNum:
            sum += num  
        
        if isGear:
            if gearLocation not in gear:
                gear[gearLocation] = [num]
            else:
                gear[gearLocation].append(num)
 
for key in gear:
    if len(gear[key]) == 2:
        total += gear[key][0]*gear[key][1]

print(total)