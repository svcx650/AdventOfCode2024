### open input
with open('testinput.txt', 'r') as file:
    lines = file.read().splitlines()


# create a list of unique frequencies
#for each item in list of unique frequencies:
## find locations of antennas
## calculate locations of antinodes and store on antiNode map
# count antinodes from map


### find answer
results = []


### report answer
print('Answer:', sum(results))