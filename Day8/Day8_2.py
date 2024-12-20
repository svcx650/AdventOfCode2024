def AntiNodeFinder(antenna, nextAntenna, rowMax, columnMax):
    possibleAntinodes = []
    distance = nextAntenna[0]-antenna[0], nextAntenna[1]-antenna[1]
    current = antenna
    while current[0] <= rowMax and current[1] <= columnMax:
        possibleAntinodes.append(current)
        current = (current[0] + distance[0], current[1] + distance[1])
    current = antenna
    while current[0] >= 0 and current[1] >= 0:
        possibleAntinodes.append(current)
        current = (current[0] - distance[0], current[1] - distance[1])
    return possibleAntinodes



### open input
with open('testinput.txt', 'r') as file:
    lines = file.read().splitlines()
mappedArea = [list(line) for line in lines]
rowMax = len(mappedArea)-1
columnMax = len(mappedArea[0])-1


### find answer

# create a list of unique frequencies
frequencies = {freq for row in mappedArea for freq in row}
frequencies.discard('.')
frequencies = list(frequencies)
# print(frequencies)

# find antenna locations
antLocs = {} # stores frequency and list of location tuples of that frequency
for frequency in frequencies:
    antLocs[frequency] = []
    for rowIndex, row in enumerate(mappedArea):
        searchIndex = 0
        rowString = ''.join(row)
        while searchIndex < len(rowString):
            antenna = None
            columnIndex = rowString.find(frequency, searchIndex)
            if columnIndex == -1: break # exit loop if no more instances of the frequency
            searchIndex = columnIndex + 1
            antenna = rowIndex, columnIndex
            antLocs[frequency].append(antenna)

# find locations of antinodes
antiNodes = []
for frequency in antLocs:
    antennaCoords = antLocs[frequency]
    for index, antenna in enumerate(antennaCoords):
        for nextAntenna in antennaCoords[index+1:]:
            antiNodes.extend(AntiNodeFinder(antenna, nextAntenna, rowMax, columnMax))

    print(frequency,len(antiNodes))
print('frequency, frequency antinodes (not de-duped)')
        # calculate antinode locations for each remaining antenna location
        # check that antinode locations are within the mapped area
        # add antinode location to list if not already in there

for i in sorted(list(set(antiNodes)), key=lambda x: (x[0], x[1])):
    print(i)


# count antinodes from map
# result = 0
# for line in antinodeMap:
#     increment = line.count('#')
#     result += increment

# ### report answer
print('Answer:', len(set(antiNodes)))