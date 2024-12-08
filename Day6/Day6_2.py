import time

def Joiner(listofListsofChars): # tested
    output = []
    for value in listofListsofChars:
        line = ''.join(value)
        output.append(line)
    return output

### open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

mappedArea = [list(line) for line in lines] # transposes to make matrix that is like searching original matrix vertically

### find starting position and orientation
orientation = 0 # known starting orientation, degrees, 0 is north, 90 is east, etc.

orientIncrement = {0:(-1,0), 90:(0,1), 180:(1,0), 270:(0,-1)}
    # up, north, 0 means increment row 1
    # down, south, 180 means increment row by -1
    # left, west, 270 means increment column by -1
    # right, east, 90means increment column by 1

for row, line in enumerate(lines):
    column = line.find('^')
    if column == -1: continue
    currentPosition = [row, column]
    break
    

### move until obstruction, adjust orientation, mark path, continue until boundary
thruBoundary = False
loopCount = 0
while thruBoundary == False:
    # print(loopCount)
    # time.sleep(3)
    if loopCount == 0: startPosition = currentPosition # on second loop this needs to be set to last position
    else: startPosition = lastPosition
    obstruction = False
    while obstruction == False:
        lastPosition = currentPosition[:]
        # print(lastPosition)
        # time.sleep(1)
        currentPosition[0] = lastPosition[0] + orientIncrement[orientation][0] # increment rows based on orientation
        currentPosition[1] = lastPosition[1] + orientIncrement[orientation][1] # increment columns based on orientation
        try:
            currentChar = lines[currentPosition[0]][currentPosition[1]]
            #check position values for '#'
            if currentChar == '#':
                obstruction = True
                currentPosition = lastPosition[:]
                # print('obstruction found, rotating at',currentPosition)
        except IndexError:
            thruBoundary = True
            currentPosition = lastPosition[:]
            break
        # mark path with 'X'
        mappedArea[currentPosition[0]][currentPosition[1]] = 'X'

    # adjust orientation
    if orientation == 270: orientation = 0
    else: orientation += 90
    loopCount += 1

mappedArea = [''.join(line) for line in mappedArea]
for m in mappedArea:
    print(m)

### find answer
# count distinct positions, including start position
result = 0
for line in mappedArea:
    increment = line.count('X')
    result += increment

### report answer
print('Answer:', result)