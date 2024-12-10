def TrailFinder(position, row, column, up, down, left, right)

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
    for column, position in line:
        score = 0
        trail = []
        if position == 0:
            # begin checking for trails
            # try all directions
            ## for any valid directions that equal position += 1 
            ## store coordinates in trail as tuple if it does not already exist in trail

            # increment score until all trails have been scored
            scores.append(score)


# ### report answer
# print('Answer:', sum(scores))