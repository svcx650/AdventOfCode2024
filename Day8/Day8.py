### open input
with open('testinput.txt', 'r') as file:
    lines = file.read().splitlines()
mappedArea = [list(line) for line in lines] # transposes to make matrix that is like searching original matrix vertically

### find answer
# create a list of unique frequencies
frequencies = []
for row in mappedArea:
    frequencies.extend(row)
frequencies = list(set(frequencies))
frequencies.pop(frequencies.index('.'))
print(frequencies)

# find antenna locations
antLocs = {}
for frequency in frequencies:
    antLocs[frequency] = []
    for rowindex, row in mappedArea:
        searchIndex = 0
        while searchIndex < len(row)
            columnIndex = row.find(frequency, searchIndex)
            if columnIndex == -1: break

#for each item in list of unique frequencies:
## find locations of antennas
## calculate locations of antinodes and store on antinodeMap as '#''


# count antinodes from map
# result = 0
# for line in antinodeMap:
#     increment = line.count('#')
#     result += increment

# ### report answer
# print('Answer:', sum(results))