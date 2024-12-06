### open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()


### find answer
count_xmases = 0
indices = []
for index, line in enumerate(lines):
    if index == 0: continue # skip first line
    if index == (len(lines)-1): continue # skip last line
    for dex, char in enumerate(line):
        if dex == 0: continue # skip first element
        if dex == (len(line)-1): continue # skip last element
        aCheck = ''
        bCheck = ''
        if char == 'A': # find an 'A'
            aCheck = aCheck + lines[index-1][dex-1]
            aCheck = aCheck + 'A'
            aCheck = aCheck + lines[index+1][dex+1]
            bCheck = bCheck + lines[index-1][dex+1]
            bCheck = bCheck + 'A'
            bCheck = bCheck + lines[index+1][dex-1]
            # print('for ', index, ',', dex, 'a:',aCheck,'b:',bCheck)
            if aCheck == 'SAM' or aCheck == 'MAS':
                if bCheck == 'SAM' or bCheck == 'MAS':
                    count_xmases += 1
                    coords = index,dex
                    indices.append(coords)
            # use index to check line above and line below for Ms and Ss, make sure that MAM or SAS isn't counted


### report answer
# print(indices)
print('Total Count:', count_xmases)