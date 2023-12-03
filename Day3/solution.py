import numpy as np 

data = open('input.txt').read().split('\n')
data = [list(row) for row in data]

schematic = np.array(list(data), dtype=np.dtype(str))
schematic = np.pad(schematic, 1, mode='constant', constant_values=['.'])

def hasSymbol(row, col, length):
    section = schematic[row-1:row + 2, col-1:col + length + 1]

    top = np.all(section[0,:] == '.')
    bottom = np.all(section[2,:] == '.')
    left = np.all(section[:,0] == '.')
    right = np.all(section[:,-1] == '.')

    return not all([top, bottom, left, right])

shape = schematic.shape
total = 0
gears = []
for row in range(shape[0]):
    col = 0
    while col < shape[1]:
        if ''.join(schematic[row, col:col+3]).isnumeric():
            gears.append([row, col, 3])
            col += 3
        elif ''.join(schematic[row, col:col+2]).isnumeric():
            gears.append([row, col, 2])
            col += 2
        elif ''.join(schematic[row, col:col+1]).isnumeric():
            gears.append([row, col, 1])
            col += 1
        else:
            col += 1

gears = [[row, col, length] for row, col, length in gears if hasSymbol(row, col, length)]
answer = sum([int(''.join(schematic[row, col:col+length])) for row, col, length in gears])
print(f'part 1: {answer}')

stars = [[row, col] for row in range(shape[0]) for col in range(shape[1]) if schematic[row, col] == '*']

gearRatios = 0
for rowStar, colStar in stars:
    neighbors = [[r, c, l] for r, c, l in gears if r - 1 <= rowStar <= r + 1 and c - 1 <= colStar <= c + l]
    if len(neighbors) == 2:
        values = [int(''.join(schematic[row, col:col+length])) for row, col, length in neighbors]
        gearRatios += values[0] * values[1]

print(f'part 2: {gearRatios}')