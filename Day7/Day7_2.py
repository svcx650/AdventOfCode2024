def RecursiveMath(equation):
    calculatedValues = []
    for index,value in enumerate(equation):
        if index == 0:
            calculatedValues.append([value])
            continue
        plus = [value + i for i in calculatedValues[-1]]
        multiply = [value * i for i in calculatedValues[-1]]
        concat = [int(str(i)+str(value)) for i in calculatedValues[-1]]
        newEntry = plus + multiply + concat
        calculatedValues.append(newEntry)
    # print(calculatedValues)
    return calculatedValues[-1]



### open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

### format input
data = []
for line in lines:
    testValue, calibrationEq = line.split(':')
    testValue = int(testValue)
    calibrationEq = calibrationEq.split(' ')[1:]
    calibrationEq = [int(i) for i in calibrationEq]
    newEl = testValue, calibrationEq
    data.append(newEl)

## find answer
results = []
for line in data:
    output = RecursiveMath(line[1])
    if line[0] in output: results.append(line[0])

### report answer
print('Answer:', sum(results))