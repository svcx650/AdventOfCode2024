### open input
with open('input.txt', 'r') as file:
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
        possibleAntinodes = []
        for nextAntenna in antennaCoords[index+1:]:
            distance = nextAntenna[0]-antenna[0], nextAntenna[1]-antenna[1]
            aPossibleAntiNode = tuple(a - b for a, b in zip(antenna, distance))
            bPossibleAntiNode = tuple(a + b for a, b in zip(nextAntenna, distance))
            possibleAntinodes.append(aPossibleAntiNode)
            possibleAntinodes.append(bPossibleAntiNode)
        filtered_ants = [
        (a, b) for a, b in possibleAntinodes if 0 <= a <= rowMax and 0 <= b <= columnMax
        ]
        antiNodes.extend(filtered_ants)
    print(frequency,len(antiNodes))
print('frequency, frequency antinodes (not de-duped)')
        # calculate antinode locations for each remaining antenna location
        # check that antinode locations are within the mapped area
        # add antinode location to list if not already in there



# count antinodes from map
# result = 0
# for line in antinodeMap:
#     increment = line.count('#')
#     result += increment

# ### report answer
print('Answer:', len(set(antiNodes)))