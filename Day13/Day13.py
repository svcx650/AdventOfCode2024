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
with open('input.txt', 'r') as file:
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
    print(answerflt, 'to', answer)
    # fractional, integer = np.modf(answer)
    fraction = [i % 1 for i in answer]
    print(key, answer, fraction)
    if all(fraction) == 0:
        minimumButtonPresses.append(answer)
        tokensRequired += 3*answer[0] + answer[1]
        print('passed', tokensRequired)
    # print('prizePosition ', prizePosition,' answer is ',answer)

# remove answers that have decimal places and multiply the remaining by the amount of tokens
# tokensRequired = 0
# for index, machine in enumerate(minimumButtonPresses):
#     fractional, integer = np.modf(machine)
#     print(machine, fractional)
#     if all(fractional== 0.0):
#         print('pass')
#         tokensRequired += 3*machine[0] + machine[1]
#     # print(tokensRequired, machine)



# a*94 + b*22 = 8400
# a*34 + b*67 = 5400
# pizePosition = np.array([])
### find answer

# set up a system of equations
# solve the system of equations
# ....




### report answer
# print(len(stones))
