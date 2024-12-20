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
for i in range(75): # iterate for each blink
    newstones = {} # temp container for stones created in this blink
    for stone in stones: # iterate through each numbered stone (critically not iterating on multiple instances of the same numbered stone)
        newestStones = [] # container for new stone(s) created from 'stone'
        # create/modify stones according to blink rules
        if stone == 0: newestStones.append(1)
        elif len(str(stone)) % 2 == 0:
            string = str(stone)
            a = int(string[:int((len(string)/2))])
            b = int(string[int((len(string)/2)):])
            newestStones.append(a)
            newestStones.append(b)
        else: newestStones.append(stone*2024)
        
        # check if child stone(s) already exist in the dictionary, increment if they do, new insertion if they don't
        # incrementing by the instance count of the parent stone is the key
        for instance in newestStones:
            if instance in newstones: newstones[instance] += stones[stone] 
            else: newstones[instance] = stones[stone]
    stones = newstones.copy()
    print('Completed blink', i+1)


### archive
# for i in range(30): # enter blinks in range
#     newstones = {}
#     for stone in stones:
#         for count in range(stones[stone]):
#             newestStones = []
#             if stone == 0: newestStones.append(1)
#             elif len(str(stone)) % 2 == 0:
#                 string = str(stone)
#                 a = int(string[:int((len(string)/2))])
#                 b = int(string[int((len(string)/2)):])
#                 newestStones.append(a)
#                 newestStones.append(b)
#             else: newestStones.append(stone*2024)
#             for instance in newestStones:
#                 if instance in newstones: newstones[instance] += 1
#                 else: newstones[instance] = 1
#     stones = newstones.copy()
#     print('Completed blink', i+1)



### report answer
numStones = 0
for stone in stones:
    numStones += stones[stone]
print(numStones)


# 40 blinks for part 1 code: 76.6s
# 40 blinks for dictionary (1 level): 71s
# 25 blinks part1 on home pc 310ms
# 35 blinks part1 on home pc 14.8s (11962408)
# 35 blinks part2_2 on home pc 15.7s
# 35 blinks part2_2 on work pc 9.9s