def blink(stones, numberofblinks):
    for i in range(numberofblinks):
        newstones = []
        for index, stone in enumerate(stones):
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
        stones = newstones[:]
    print(i)
    return len(stone)


### open input
with open('test2input.txt', 'r') as file:
    line = file.read().splitlines()

### format input
stones = [int(i) for i in line[0].split(' ')]

### find answer
totalLength = 0
for stone in stones:
    totalLength += blink([stone], 75)






# blink25 = blink(stones, 25)
# print('completed 25 blinks, Number of stones:', stones)

# startindex = 0
# stopindex = 16
# sectionsOfStones = []
# while stopindex <= len(blink25):
#     # print(stopindex)
#     newList = blink25[startindex:stopindex]
#     sectionsOfStones.append(newList)
#     startindex = stopindex
#     stopindex += 16

# print("made sectionsOfStones. It's length is: ",len(sectionsOfStones))

# blink50 = []
# for i in sectionsOfStones:
#     blink50.append(blink(i, 25))
# print('finished blink50')
# totalLength = 0
# for length in blink50:
#     totalLength += len(length)

### report answer
print(totalLength)