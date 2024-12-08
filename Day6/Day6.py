### open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

### find starting position and orientation
orientation = 0 # known starting orientation, degrees, 0 is north, 90 is east, etc.
for row, line in enumerate():
    try:
        column = line.find('^')
    except: continue
    position = [row, column]

### move until obstruction, adjust orientation, mark path, continue until boundary
thruBoundary = False
while thruBoundary == False:
    startPos = position
    startOr = orientation
    obstruction = False
    while obstruction == False:
        position = #update position, maybe not needed? could just find next pos until obstruction/boundary then store next pos-1 in end position
        try:
            nextPos = # increment based on orientation
                ## may need to break this out by up, down, left, right
        except IndexError:
            # nextPos stays as the current pos because reassigning was unsuccessful
            thruBoundary = True
            break
        if nextPos == '#':
            obstruction = True
            # adjust orientation
    # modify past positions in mappedArea with 'X'


### find answer
# count distinct positions, including start position
result = 0
for line in mappedArea:
    increment = line.count('X')
    result += increment
#### BE SURE TO INCLUDE: start position and END POSITION (UP TO BOUNDARY)

# report answer
print(result)


