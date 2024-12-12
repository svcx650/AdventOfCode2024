### open input
with open('test2input.txt', 'r') as file:
    line = file.read().splitlines()

### format input
stones = [int(i) for i in line[0].split(' ')]

### find answer
allstones = [stones]
for i in range(40):
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
    print(i)

### report answer
print(len(stones))
stoned = [set(l) for l in allstones]
print(len(stoned))