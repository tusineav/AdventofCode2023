import numpy as np

file = open("input.txt", "r")

lines = file.readlines()

symbols = ""
for i in range(0, len(lines)):
    lines[i] = lines[i].replace("\n", "")
    symbols += lines[i]

for digit in range(0, 10):
    symbols = symbols.replace(str(digit), "")

symbols = list(set(symbols.replace(".", "")))

gears = {}
for row, line in enumerate(lines):
    start = 0
    while start < len(line):
        if '1' <= line[start] <= '9':
            numbers = line[start:]
            for symbol in symbols:
                numbers = numbers.replace(symbol, " ")
            
            numbers = numbers.replace(".", " ")
            numbers = ' '.join(numbers.split())
            number = numbers.split(" ")[0]
            
            end = start + len(number)

            stop = False
            for i in range(max(0, row - 1), min(len(lines), row + 2)):
                if stop:
                    break
                for j in range(max(0, start - 1), min(end + 1, len(line))):
                    if lines[i][j] in symbols:
                        stop = True
                        #This time it's a bit different. If we come across a *, add to a dict: 1. the index as a key, 2. the numbers its attached to
                        if lines[i][j] == "*":
                            if (i, j) not in gears:
                                gears[(i, j)] = [int(number)]
                            else:
                                gears[(i, j)].append(int(number))
            
            start = end
        
        start += 1

gear_products = 0
for key in gears:
    if len(gears[key]) == 2:
        gear_products += gears[key][0] * gears[key][1]
        
print(gear_products)