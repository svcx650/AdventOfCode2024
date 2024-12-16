### open input
with open('input.txt', 'r') as file:
    line = file.read().splitlines()

### format input
stones = [int(i) for i in line[0].split(' ')]

### find answer

# for each stone, check dictionary keys and use value for building next list of stones
# test and compare run time (not a huge improvement)
# further optimization: rather than a list of all stones, use a dictionary
# where each key is a stone with a number and the value is the number of stones with that number


numbers = {}
for i in range(40/5): # enter blinks in range
    newstones = []
    for index, stone in enumerate(stones):
        if stone in numbers:
            newstones.append(numbers[stone])
        else:
            if stone == 0:
                newstones.append(1)
                continue
            elif len(str(stone)) % 2 == 0:
                string = str(stone)
                a = int(string[:int((len(string)/2))])
                b = int(string[int((len(string)/2)):])
                newstones.append(a)
                newstones.append(b)
                continue
            else:
                newstones.append(stone*2024)
            numbers[stone] = newstones[-1]
    stones = newstones[:]
    allstones.append(stones)
    print('Completed blink', i+1)

### report answer
print(len(stones))
stoned = {l for k in allstones for l in k}
# stoned = set(stoned)
print(len(stoned))
# print(numbers)

# 40 blinks for part 1 code: 76.6s
# 40 blinks for dictionary (1 level): 71s