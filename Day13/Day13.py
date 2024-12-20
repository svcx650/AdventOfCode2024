import numpy as np

def FindNumbers(line, indicator):
    unused, containsFirstNum, secondNum = line.split(indicator)
    firstNum = ''
    for char in containsFirstNum:
        try:
            int(char)
            firstNum = firstNum + char
        except: break
    return int(firstNum), int(secondNum)


### open input
with open('testinput.txt', 'r') as file:
    lines = file.read().splitlines()

### format input
machines = {}
tempMachine = []
for index, line in enumerate(lines):
    if len(line) < 3:
        machines[tuple(tempMachine[-2:])] = np.array([[ tempMachine[0],tempMachine[2] ], [ tempMachine[1],tempMachine[3] ]])
        tempMachine = [] # indicates a new machine
        continue
    if line[:5] == 'Prize':
        indicator = '='
    else: indicator = '+'
    tempMachine.extend(FindNumbers(line, indicator))
    if index == (len(lines)-1):
        machines[tuple(tempMachine[-2:])] = np.array([[ tempMachine[0],tempMachine[2] ], [ tempMachine[1],tempMachine[3] ]])
        tempMachine = [] 
print(machines)
# solve systems of equations
minimumButtonPresses = []
tokensRequired = 0
for key in machines:
    prizePosition = np.array(list(key))
    equations = machines[key]
    answerflt = np.linalg.solve(equations, prizePosition)
    answer = []
    for i in answerflt:
        if i % 1 < 0.0001: answer.append(int(i))
        elif 0.9999 <= i % 1 <= 1.001: answer.append(int(i+1))
        else: answer.append(i)
    # print(answerflt, 'to', answer)
    # fractional, integer = np.modf(answer)
    fraction = [i % 1 for i in answer]
    # print(key, answer, fraction)
    if all(fraction) == 0:
        minimumButtonPresses.append(answer)
        tokensRequired += 3*answer[0] + answer[1]

### report answer
print('Answer:', tokensRequired)