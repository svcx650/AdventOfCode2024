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
    return muls

def Multiplier(mul):
    a , b = mul.split(',') # split at ','
    a, b = a[4:],  b[:-1] # strip 'mul(' and ')'
    a, b = int(a), int(b) # convert number strings to int
    return a * b 

def DoOrDont(megaLine, allMuls):
    results = []
    scanIndex = 0
    enabled = True
    workingIndex = 0
    while scanIndex <= len(megaLine):
        if enabled:
            workingIndex = megaLine.find("don't()")
            # turn working index into mul index
            
            # process muls and append
            for mul in enabledMuls:
                results.append(Multiplier(mul))
            
            enabled = False ### Nothing goes in if statement below here
        else:
            megaLine.find("do()")
            # turn working index into mul index
            # discard muls
            enabled = True ### Nothing goes in else statement below here
        ### Nothing goes in while statement below here


    return(results)


# open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

# format input
muls = []
mulsbyline = []
for line in lines:
    output = FindMuls(line)
    muls.extend(output)
    mulsbyline.append(output)


# find answer
enabledMuls = []
### need to handle the enabling/disabling
# make a mega string, give it to DoOrDont, DoOrDont uses multiplier, out comes results
# use DoOrDont()
# enable vs disabled needs to persist between lines

results = DoOrDont(megaLine, muls)

# report answer
print(sum(results))