def TrailFinder(position, mappedArea):
    nextSteps = []
    try:
        up = (row-1,column)
        trail.append(up)
    except IndexError: pass
    try:
        down = (row+1,column)
        trail.append(down)
    except IndexError: pass
    try:
        left = (row,column-1)
        trail.append(left)
    except IndexError: pass
    try:
        right = (row,column+1)
        trail.append(right)
    except IndexError: pass
    return nextSteps


### open input
with open('testinput.txt', 'r') as file:
    lines = file.read().splitlines()

### format input
mappedArea = []
for line in lines:
    newline = [int(digit) for digit in line]
    mappedArea.append(newline)

### find answer
# for each 0, find all trails that end in 9 (incrementing by 1, moving up down left right)
scores = []
for row, line in mappedArea:
    for column, char in line:
        score = 0
        trail = []
        if char == 0:
            position = (row,column)
        nextSteps = [1]
        while nextSteps != []
            nextSteps = []
            nextSteps = TrailFinder(position, mappedArea)
            for step in nextSteps:
                step
            for location in trail:
                #check other locations




            while
            # begin checking for trails
            try: up == 
            # try all directions
            ## for any valid directions that equal position += 1 
            ## store coordinates in trail as tuple if it does not already exist in trail

            # increment score until all trails have been scored
            scores.append(score)


# ### report answer
# print('Answer:', sum(scores))