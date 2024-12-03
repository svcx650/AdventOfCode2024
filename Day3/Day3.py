
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
            searchIndex = startIndex + 9 # minimum number of characters to skip that could be a valid mul(
            # print('search index is now ', searchIndex)

    # now startIndices contains the indices of all the m's in 'mul(' that could be valid.
    if startIndices == []:
        # print('no mul( found on this line')
        return muls
    print(startIndices)
    for index in startIndices:
        endIndex = None
        testString = line[index:index+12] # 12 is length needed to include longest valid mul (with closing parenthesis)
        try: a, b = testString.split(',')
        except ValueError:
            # print('no , found for start index ',index,' which is test string ', testString)
            continue

        a_check = []
        for char in a[4:]:
            try: a_check.append(int(char))
            except ValueError: break
        if len(a_check) > 0 and len(a_check) < 4:
            if len(a_check) == len(a[4:]): # check that number doesn't have invalid chars between it and the , that was previously split out
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

        # no continues by this point should mean it's a valid mull
        # print('mul found for start index ', index)
        endIndex = index + endIndex # now is a true index
        mul = line[index:endIndex]
        print('found mul(', firstNumber, ',', secondNumber,')')
        print('appending: ',mul)
        muls.append(mul)
    return muls

def Multiplier(mul):
    a , b = mul.split(',') # split at ','
    a, b = a[4:],  b[:-1] # strip 'mul(' and ')'
    a, b = int(a), int(b) # convert number strings to int
    return a * b 


# open input
with open('shortinput.txt', 'r') as file:
    lines = file.read().splitlines()


# format input
muls = []
count_muls = 0
for line in lines:
    output = FindMuls(line)
    count_muls += 1
    # print(output)
    muls.extend(output)


# find answer
results = []
for i in muls:
    results.append(Multiplier(i))


# report answer
# print(results)
# print('len of lines', len(lines))
# print('len of muls', len(muls))
# print(count_muls)
# print('len of results', len(results))
print(sum(results))