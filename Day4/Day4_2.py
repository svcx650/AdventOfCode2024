import math

def FindXMAS(line):  # accepts a string and finds matches of MAS or SAM, stores index of A in either case into 1 list
    a_line_indices = []

    Criteria = 'MAS'
    searchIndex = 0
    minSearchLength = len(Criteria)

    while searchIndex < len(line): # exits if remaining string cannot contain the criteria
        xmas = line.find(Criteria, searchIndex)
        if xmas != -1:
            a_line_indices.append(xmas+1)
            searchIndex = xmas + 1
        else:
            searchIndex = len(line)
            continue


    Criteria = 'SAM'
    minSearchLength = len(Criteria)
    searchIndex = 0

    while searchIndex < len(line): # exits if remaining string cannot contain the criteria
        xmas = line.find(Criteria, searchIndex)
        if xmas != -1:
            a_line_indices.append(xmas+1)
            searchIndex = xmas + 1
        else:
            searchIndex = len(line)
            continue
    return a_line_indices



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



### open input
with open('test1input.txt', 'r') as file:
    lines = file.read().splitlines()


# rotate the input so we check along diagonals
diag1 = Joiner(Rotate45(lines,'r'))
diag2 = Joiner(Rotate45(lines,'l'))
rotatedinput = [diag1, diag2]

### find answer
# find sam or mas in diag 1, record index of A for either case in 1 list
allIndices = [] # becomes [[a coords matrix 1],[a coords matrix 2]]
for index, matrix in enumerate(rotatedinput):
    for i in matrix:
        print(i)
    matrix_indices = []
    for diag_index, line in enumerate(matrix):
        a_indices = []
        a_indices = FindXMAS(line)
        full_line_indices = [[diag_index,i] for i in a_indices]
        matrix_indices.extend(full_line_indices)
    allIndices.append(matrix_indices)

diag1_indices = allIndices[0]
diag2_indices = allIndices[1]
print(diag1_indices)

reg_coords = []
for coords in diag1_indices:
    rp, cp = coords[0] , coords[1] #row prime, column prime
    r = int(round((rp + cp)/math.sqrt(2),0))
    c = int(round((cp - rp)/math.sqrt(2),0))
    reg_coord = [r, c]
    reg_coords.append(reg_coord)
print(reg_coords)

# convert A_line_indices from diag 1 or 2 into terms of the other, compare, count matches, that's the answer
count_xmas_s = 0


### report answer

print('Total Count:', count_xmas_s)