def FindMuls(line):
    muls = []
    startIndices = []
    searchIndex = 0
    while searchIndex < (len(line) - 8): # exits if remaining string to search cannot contain a valid mul
        startIndex = line.find('mul(', searchIndex)
        if startIndex == -1:
            searchIndex = len(line)
            continue
        else:
            startIndices.append(startIndex)
            searchIndex = startIndex + 4 # minimum number of characters to skip that could be a valid mul(

    # now startIndices contains the indices of all the m's in 'mul(' that could be valid.
    if startIndices == []:
        return muls
    returnIndices = []
    for index in startIndices:
        endIndex = None
        testString = line[index:index+12] ########### 12 is length needed to include longest valid mul (with closing parenthesis)
        
        # find and remove cases of 2 commas in testString which was causing me to miss 3 muls
        if testString.count(',') > 1:
            clipIndex = testString[::-1].find(',')
            testString = testString[:-(clipIndex+1)]
        try: a, b = testString.split(',')
        except ValueError:
            continue

        a_check = []
        for char in a[4:]:
            try: a_check.append(int(char))
            except ValueError: break
        if len(a_check) > 0 and len(a_check) < 4:
            if len(a_check) == len(a[4:]): # check that 'a' number doesn't have invalid chars between it and the , that was previously split out
                firstNumber = ''
                for i in a_check:
                    firstNumber = firstNumber + str(i)
                firstNumber = int(firstNumber)
            else:
                continue
        else:
            continue
        endIndex = len(a) + 1 # increment from index to comma


        secondNumber = b.split(')')[0]
        if len(secondNumber) == len(b):
            continue
        endIndex += len(secondNumber) + 1 # increment from index to close parenthesis
        try: secondNumber = int(secondNumber)
        except ValueError:
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
        endIndex = index + endIndex # now is a true index
        mul = line[index:endIndex]
        muls.append(mul)
        returnIndices.append(index)
    return muls, returnIndices

def Multiplier(mul):
    a , b = mul.split(',') # split at ','
    a, b = a[4:],  b[:-1] # strip 'mul(' and ')'
    a, b = int(a), int(b) # convert number strings to int
    return a * b 

def DoOrDont(megaString, allMuls, mulIndices):
    results = []
    scanIndex = 0
    enabled = True
    workingIndex = 0
    lastWI = 0
    lastDoIndex = 0
    
    # parse entire mega string for only the relevant do's and donts (first do after a dont and vice versa)
    while scanIndex < len(megaString):
        lastWI = workingIndex
        if enabled:
            # if enabled, look for end of enablement (next dont), then process muls up to that point
            workingIndex = megaString.find("don't()", lastWI)

            #process muls from the last "do" found, up to the "don't" we just found
            for index, value in enumerate(mulIndices): #careful here because the values are indexes of the muls in the main string
                if value > lastDoIndex and value < workingIndex:
                    results.append(Multiplier(allMuls[index]))
            enabled = False ### Nothing goes in if statement below here
        
        else: # else we're not enabled, look for when we will be
            workingIndex = megaString.find("do()", lastWI)
            lastDoIndex = workingIndex # to be used as lower bound for muls that should be processed
            enabled = True ### Nothing goes in else statement below here
        
        # handle when do() or don't() isn't found (we're at the end of the mega string, close out accordingly)
        if workingIndex == -1:
            if enabled == False:
                for lin, lval in enumerate(mulIndices): #careful here because the values are indexes of the muls in the main string
                    if lval > lastWI:
                        results.append(Multiplier(allMuls[lin]))
            scanIndex = len(megaString) # ends while loop
        else: scanIndex = workingIndex + 1
    return results


# open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()


# store values needed to go from mul index within a line to within the mega string
lineLengths = [0]
cum_line_start_index = []
for p in lines:
    lineLengths.append(len(p))
for index, value in enumerate(lineLengths):
    newValue = sum(lineLengths[:index])
    cum_line_start_index.append(newValue)
cum_line_start_index = cum_line_start_index[1:]

# parse muls and mul indices
muls = []
mulIndices = []
for index, line in enumerate(lines):
    returnedIndices = []
    output = None
    output, returnedIndices = FindMuls(line)
    returnedIndices = [i + cum_line_start_index[index] for i in returnedIndices]
    mulIndices.extend(returnedIndices)
    muls.extend(output)

# find answer
# make a mega string, give it to DoOrDont, DoOrDont uses multiplier, out comes results
megaString = ''.join(lines)
results = DoOrDont(megaString, muls, mulIndices)

# report answer
print('answer: ',sum(results))