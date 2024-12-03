# open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

elves = []
currentElf = 0
for line in lines:
    try: currentElf += int(line)
    except:
        elves.append(currentElf)
        currentElf = 0
# report
print(max(elves))