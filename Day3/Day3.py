
def FindMuls(line):
    muls = []
    startIndices = []
    searchIndex = 0
    while searchIndex < (len(line) - 8): # exits if remaining string to search cannot contain a valid mul
        # print('starting loop with searchindex ', searchIndex)
        startIndex = line.find('mul(', searchIndex)
        if startIndex == -1:
            searchIndex = len(line)
            continue
        else:
            # print('appending ', startIndex)
            startIndices.append(startIndex)
            searchIndex = startIndex + 4 # minimum number of characters to skip that could be a valid mul(
            # print('search index is now ', searchIndex)

    # now startIndices contains the indices of all the m's in 'mul(' that could be valid.
    if startIndices == []:
        # print('no mul( found on this line')
        return muls
    # print(startIndices)
    for index in startIndices:
        endIndex = None
        testString = line[index:index+12] ########### 12 is length needed to include longest valid mul (with closing parenthesis)
        try: a, b = testString.split(',')
        except ValueError:
            # print('no , found for start index ',index,' which is test string ', testString)
            continue
# mul(    456     789    )
        a_check = []
        for char in a[4:]:
            try: a_check.append(int(char)) ########## special char parsed as number?
            except ValueError: break
        if len(a_check) > 0 and len(a_check) < 4:
            if len(a_check) == len(a[4:]): ##### double check this, remove
            # check that number doesn't have invalid chars between it and the , that was previously split out
                firstNumber = ''
                for i in a_check:
                    firstNumber = firstNumber + str(i)
                firstNumber = int(firstNumber)
                # print('found first number ', firstNumber, ' for start index ', index)
            else:
                # print('invalid first number (len incorrect) for start index ', index)
                continue
        else:
            # print('invalid first number (too short/long) for start index ', index)
            continue
        endIndex = len(a) + 1 # increment from index to comma


        secondNumber = b.split(')')[0]
        if len(secondNumber) == len(b):
            # print('no ) found for start index ', index)
            continue
        endIndex += len(secondNumber) + 1 # increment from index to close parenthesis
        try: secondNumber = int(secondNumber)
        except ValueError:
            # print('invalid second number ',secondNumber, ' for start index ', index)
            continue

        secondNumber = b.split(')')[0]
        b_secondNumber_check = []
        for char in secondNumber:
            try: b_secondNumber_check.append(int(char)) ########## special char parsed as number?
            except ValueError: break
        if len(b_secondNumber_check) > 0 and len(b_secondNumber_check) < 4:
            secondNumString = ''
            for i in b_secondNumber_check:
                secondNumString = secondNumString + str(i)
        else: continue


        # no continues by this point should mean it's a valid mull
        # print('mul found for start index ', index)
        endIndex = index + endIndex # now is a true index
        mul = line[index:endIndex]
        print('found mul(', firstNumber, ',', secondNumber,')')
        print('appending: ',mul)
        muls.append(mul)
    # print('startindices', startIndices)
    return muls

def Multiplier(mul):
    a , b = mul.split(',') # split at ','
    a, b = a[4:],  b[:-1] # strip 'mul(' and ')'
    a, b = int(a), int(b) # convert number strings to int
    return a * b 

def rmMuls(muls,line):
    cleanline = line
    for i in muls:
        cleanline = cleanline.replace(i,'')
    return cleanline


# open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

# format input
muls = []
mulsbyline = []
for line in lines:
    output = FindMuls(line)
    muls.extend(output)
    # print('output len', len(output))
    mulsbyline.append(output)


# find answer
results = []
for i in muls:
    results.append(Multiplier(i))

# # show input less the found muls for debugging
# cleanedInput = []
# for index, mbl in enumerate(mulsbyline):
#     cleanedLine = rmMuls(mbl, lines[index])
#     # print('cleanedLine', cleanedLine)
#     cleanedInput.append(cleanedLine)
# for i in cleanedInput: print(i)
# numspaceparen = 0
# numspacecomma = 0
# commaspacenum = 0
# for line in lines:
#     numspaceparen = line.count(' )')
#     numspacecomma = line.count(' ,')
#     commaspacenum = line.count(', ')
#     foundindex = line.find(' )')
#     print(line[foundindex-4:foundindex+2])
    # print('numspaceparen',numspaceparen)
    # print('numspacecomma',numspacecomma)
    # print('commaspacenum',commaspacenum)


# report answer
# print('len of lines', len(lines))
# print('len of muls', len(muls))
# print('len(muls)', len(muls))
# print(results)
print(sum(results))