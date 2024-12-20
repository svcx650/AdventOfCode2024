import numpy as np
import sympy as sp

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

'''
a*94 + b*22 = 8400
a*34 + b*67 = 5400
system = [
    Eq(94*a + 22*b, 8400),
    Eq(34*a + 67*b, 5400)
]
soln = solve(system, [x, y])
print(soln)

tempMachine = [94, 34, 22, 67, 8400, 5400]
'''

a, b = sp.symbols(['a','b'])
machines = []
tempMachine = []

for line in lines:
    # parse numbers from input and add to holding list until we have enough to make the system of equations
    if len(line) < 3: continue # skip empty lines
    if line[:5] == 'Prize':
        indicator = '='
    else: indicator = '+'
    print('Finding numbers...')
    tempMachine.extend(FindNumbers(line, indicator))

    # if we have all the numbers needed, create the system and reset holding list
    if len(tempMachine) == 6:
        system = [
            sp.Eq(tempMachine[0]*a + tempMachine[2]*b, tempMachine[4]+10000000000000),
            sp.Eq(tempMachine[1]*a + tempMachine[3]*b, tempMachine[5]+10000000000000)
        ]
        machines.append(system)
        system = []
        tempMachine = []

# solve systems of equations
minimumButtonPresses = []
for sys in machines:
    answer = sp.solve(sys, [a, b])
    minimumButtonPresses.append(answer)
    print(answer)

'''
Minimum button presses is list of 
{a: 80, b: 40},
{a: 137021/969, b: 131198/969}
'''

# filter equations that aren't solvable (with integers)
tokensRequired = 0
for ans in minimumButtonPresses:
    if '/' not in str(ans[a]) and '/' not in str(ans[b]):
        tokensRequired += 3*ans[a] + ans[b]

### Report answer
print('Answer:', tokensRequired)