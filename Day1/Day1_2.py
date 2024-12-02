
# open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

# format input
leftList = []
rightList = []
for line in lines:
    left, right = line.split()
    leftList.append(int(left))
    rightList.append(int(right))

# find answer
simScores = []
for value in leftList:
    sim = None
    rightListOcc = rightList.count(value)
    sim = value * rightListOcc
    simScores.append(sim)

# report answer
print('result: ',sum(simScores))