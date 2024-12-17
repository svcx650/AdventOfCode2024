### open input
with open('input.txt', 'r') as file:
    line = file.read().splitlines()

### format input
stones = [int(i) for i in line[0].split(' ')]

### find answer
allstones = [stones]
for i in range(35): # enter blinks in range
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
    allstones.append(stones)
    print('Completed blink', i+1)

### report answer
print(len(stones))
# stoned = [set(l) for l in k for k in allstones]
# stoned = set(stoned)
# print(len(stoned))