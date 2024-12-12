import numpy as np

def Blink(stones):
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
    return stones

def BlinkBlink(stones, numberofblinks):
    for i in range(numberofblinks):
        stones = Blink(stones)
        if len(stones) > 99999: # this seems to keeps it under ~1s
            print('branching after blink #', i)
            totalLength = 0
            for stone in stones:
                branchedStones = [stone]
                for x in range(numberofblinks-i-1):
                    branchedStones = Blink(branchedStones)
                totalLength += len(branchedStones)
            return(totalLength)
    return len(stones)

def archiveBlink(stones, numberofblinks):
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
        if len(stones) > 999999: # this seems to keeps it under ~1s
            print('exiting after blink #', i)
            return(len(stones), i)
    return len(stones), numberofblinks



### open input
with open('input.txt', 'r') as file:
    line = file.read().splitlines()

### format input
stones = [int(i) for i in line[0].split(' ')]



### find answer

# for each stone, blink until you get to a number of stones >20000, keeping track of number of blinks
# for each stone
# when number of stones exceeds 20000, branch off and process the stones individually, only storing the length of the stones for the branch being processed



### report answer
# print('completed blinks, Number of stones:', blink25)
blinking = BlinkBlink(stones,22) # change to 75 when ready
print(blinking)

# 238-255ms for 25 blinks on test2input.txt
# 295-356ms for 25 blinks on input.txt (183248)
# 6.2s for 35 blinks on input.txt (11962408)
# 6s for 35 blinks on input.txt
# Day11 9.7s for 38 blinks (12585458)
# this 20.4s for 38 blinks
# Day11 24.0s for 40 blinks (29115525)

### Day11 takes 23.5 seconds for 40 blinks, but casting the full list of stones to a set results in a set length of 54
# if I store the number of each number then the sum of all of that is the answer. I can also shorten the run time by not recalculating numbers that have already been calculated