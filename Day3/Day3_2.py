import time
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
        # print('no mul( found on this line')
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
    increment = 0 
    lastWI = 0
    while scanIndex < len(megaString):
        print(results)
        print(scanIndex)
        time.sleep(2)
        lastWI = workingIndex
        if enabled:
            workingIndex = megaString.find("don't()", lastWI)
            print('found dont', workingIndex)
            # process and append muls with start indices less than workingIndex
            # while mulIndices[increment] < workingIndex and mulIndices[increment] > lastWI: #reverse conditions and maybe use if to skip this > cond on first pass
            while mulIndices[increment] < workingIndex:
                # time.sleep(5)
                results.append(Multiplier(allMuls[increment]))
                increment += 1
            enabled = False ### Nothing goes in if statement below here
        else:
            workingIndex = megaString.find("do()", lastWI)
            print('found do', workingIndex)
            ####### set lower bound for mulls to be used
            enabled = True ### Nothing goes in else statement below here
        if workingIndex == -1:
            if enabled == False:
                for index, value in enumerate(mulIndices): #careful here because the values are indexes of the muls in the main string
                    if value > lastWI:
                        results.append(Multiplier(allMuls[index]))
                # while mulIndices[increment] < (len(megaString) - 3): #start this at a mul index greater than the lastWI and continue to end
                #     time.sleep(5)
                #     results.append(Multiplier(allMuls[increment]))
                #     if mulIndices[increment] == mulIndices[-1]:
                #         break # end this loop due to hitting last mul
                #     increment += 1 
            scanIndex = len(megaString) # ends while loop
            print(scanIndex)
        else: scanIndex = workingIndex + 1

    return results


# open input
with open('test2input.txt', 'r') as file:
    lines = file.read().splitlines()

# format input
muls = []
mulIndices = []
lineLengths = [0]
for p in lines:
    lineLengths.append(len(p))
for index, line in enumerate(lines):
    returnedIndices = []
    output = None
    output, returnedIndices = FindMuls(line)
    returnedIndices = [i + lineLengths[index] for i in returnedIndices]
    mulIndices.extend(returnedIndices)
    muls.extend(output)

# find answer
enabledMuls = []
megaString = ''.join(lines)
### need to handle the enabling/disabling
# make a mega string, give it to DoOrDont, DoOrDont uses multiplier, out comes results
# use DoOrDont()

results = DoOrDont(megaString, muls, mulIndices)

# # # report answer
print(sum(results))