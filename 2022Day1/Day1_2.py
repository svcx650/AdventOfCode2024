# open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

elves = []
currentElf = 0
for line in lines:
    print(line)
    print(currentElf)
    try: currentElf += int(line)
    except:
        elves.append(currentElf)
        currentElf = 0
elves.append(currentElf)

# report
print(elves)
top3 = []
top = None
for i in range(3):
    top, index = max(elves), elves.index(max(elves))
    top3.append(top)
    elves.pop(index)
    print(elves)

print(sum(top3))