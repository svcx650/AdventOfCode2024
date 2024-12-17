### open input
with open('input.txt', 'r') as file:
    line = file.read().splitlines()

### format input
listStones = [int(i) for i in line[0].split(' ')]
stones = {}
for i in listStones:
    if i in stones:
        stones[i] += 1
    else:
        stones[i] = 1
### find answer

# make a dictionary of the results of 5 iterations of each number and cache results

for i in range(35): # enter blinks in range
    newstones = {}
    for stone in stones:
        for count in range(stones[stone]):
            if stone == 0:
                if 1 in newstones: newstones[1] += 1
                else: newstones[1] = 1
                continue
            elif len(str(stone)) % 2 == 0:
                string = str(stone)
                a = int(string[:int((len(string)/2))])
                b = int(string[int((len(string)/2)):])
                if a in newstones: newstones[a] += 1
                else: newstones[a] = 1
                if b in newstones: newstones[b] += 1
                else: newstones[b] = 1
                continue
            else:
                if stone*2024 in newstones: newstones[stone*2024] += 1
                else: newstones[stone*2024] = 1
    stones = newstones.copy()
    print('Completed blink', i+1)

numStones = 0
for stone in stones:
    numStones += stones[stone]

### report answer
print(numStones)



# 40 blinks for part 1 code: 76.6s
# 40 blinks for dictionary (1 level): 71s
# 25 blinks part1 on home pc 310ms
# 35 blinks part1 on home pc 14.8s (11962408)
# 35 blinks part2_2 on home pc 15.7s