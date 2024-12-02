
# open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

leftList = []
rightList = []
for line in lines:
    left, right = line.split()
    leftList.append(int(left))
    rightList.append(int(right))

distances = []
while leftList != []:
    distance = None
    if min(leftList) > min(rightList):
        distance = min(leftList) - min(rightList)
    elif min(leftList) < min(rightList):
        distance = min(rightList) - min(leftList)
    elif min(leftList) == min(rightList):
        distance = 0
    leftList.pop(leftList.index(min(leftList)))
    rightList.pop(rightList.index(min(rightList)))
    distances.append(distance)
print('result: ',sum(distances))