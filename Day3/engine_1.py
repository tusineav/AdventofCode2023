import numpy as np

file = open("input.txt", "r")

lines = file.readlines()

symbols = ""
#Remove newlines from input, and prepare to get every symbol
for i in range(0, len(lines)):
    lines[i] = lines[i].replace("\n", "")
    symbols += lines[i]

#Remove all digits and '.' from entire input. What's left over is the list of valid symbols
for digit in range(0, 10):
    symbols = symbols.replace(str(digit), "")
symbols = list(set(symbols.replace(".", "")))

part_sum = 0
for row, line in enumerate(lines):
    start = 0
    #Bit ugly - go through character by character to find numbers
    while start < len(line):
        if '1' <= line[start] <= '9':
            #If we're at a number, remove everything else from the line to get the full num without index issues
            numbers = line[start:]
            for symbol in symbols:
                numbers = numbers.replace(symbol, " ")
            
            numbers = numbers.replace(".", " ")
            numbers = ' '.join(numbers.split())
            number = numbers.split(" ")[0]
            
            end = start + len(number)

            #At this point we have the number, and the start and end indices within the line
            
            #stop is to prevent counting the same number twice (if there are two symbols)
            stop = False
            #Loop through the surrounding rectangle and count if a symbol is found
            for i in range(max(0, row - 1), min(len(lines), row + 2)):
                if stop:
                    break
                for j in range(max(0, start - 1), min(end + 1, len(line))):
                    if lines[i][j] in symbols:
                        stop = True
                        part_sum += int(number)
                        
                        break
        
        #handle properly updating the indices
            start = end
        
        start += 1

        
print(part_sum)