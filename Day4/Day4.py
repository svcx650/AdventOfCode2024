
def FindXMAS(line):  # accepts a string and finds matches of searchCriteria
    countxmases = 0
    searchIndex = 0
    Criteria = 'XMAS'
    minSearchLength = len(Criteria)
    while searchIndex < (len(line) - minSearchLength): # exits if remaining string cannot contain the criteria
        xmas = line.find(Criteria, searchIndex)
        if xmas != -1:
            countxmases += 1
            print('found', Criteria,'count is now',countxmases)
            searchIndex = xmas + 1
        else:
            searchIndex = len(line)
            print(Criteria, 'not found.')
            continue
    Criteria = 'SAMX'
    minSearchLength = len(Criteria)
    searchIndex = 0
    while searchIndex < (len(line) - minSearchLength): # exits if remaining string cannot contain the criteria
        xmas = line.find(Criteria, searchIndex)
        if xmas != -1:
            countxmases += 1
            print('found', Criteria,'count is now',countxmases)
            searchIndex = xmas + 1
        else:
            searchIndex = len(line)
            print(Criteria, 'not found.')
            continue

    return countxmases



def Joiner(listofListsofChars): # tested
    output = []
    for value in listofListsofChars:
        line = ''.join(value)
        output.append(line)
    return output



def Rotate45(lines, RorL):
    rows, columns = len(lines), len(lines[0])

    if RorL == 'r':
        max_diagonals = rows + columns - 1  # Total number of diagonals
        diagonals = [[] for _ in range(max_diagonals)]
        for j in range(rows):
            for i in range(columns):
                diagonal_key = i + j
                diagonals[diagonal_key].append(lines[i][j])
    elif RorL == 'l':
        min_diagonal = -(rows - 1)
        max_diagonal = columns - 1
        total_diagonals = max_diagonal - min_diagonal + 1
        diagonals = [[] for _ in range(total_diagonals)]
        for j in range(rows):                           ### need to fix this to rotate the other way
            for i in range(columns):
                diagonal_key = j - i - min_diagonal
                diagonals[diagonal_key].append(lines[i][j])
        diagonals = [i for i in reversed(diagonals)]

    else:
        print('invalid RorL in rotate45.')
        return None
    return diagonals



# open input
with open('testinput.txt', 'r') as file:
    lines = file.read().splitlines()


### rotate the input so we check horizontal, vertical, diagonal1, diagonal2
transposed = [[lines[j][i] for j in range(len(lines))] for i in range(len(lines))] # transposes to make matrix that is like searching original matrix vertically
### Assumes all items in 'lines' are the same length ###
vertical = Joiner(transposed)
diag1 = Joiner(Rotate45(lines,'r'))
diag2 = Joiner(Rotate45(lines,'l'))
# diag2 = [i for i in reversed(Joiner(Rotate45(lines, 'l')))]

rotatedinput = [lines, vertical, diag1, diag2] #adds horizontal (as provided input) with transformed matrices


# find answer
countxmases = 0
for matrix in rotatedinput:
    increment = 0
    for line in matrix:
        increment = 0
        increment = FindXMAS(line)
        countxmases += increment
        print(increment)


# report answer
print('Total Count:', countxmases)