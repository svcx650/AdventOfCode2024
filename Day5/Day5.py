def RuleValidator(update, rules):
    ####### checks an update for pass/fail/NA to all rules
    output = []
    for rule in rules:
        # check that update contains both pages otherwise NA
        try:
            a = update.index(rule[0])
            b = update.index(rule[1])
            if a < b:
                output.append('P')
            else: output.append('F')
        except ValueError:
            output.append('NA')
            continue
    return output


# open input
with open('testinput.txt', 'r') as file:
    lines = file.read().splitlines()


# format input
dividerIndex = 0
for index, line in enumerate(lines):
    if line == '': 
        dividerIndex = index
rules = []
for line in lines[:dividerIndex]:
    a, b = line.split('|')
    rule = int(a), int(b)
    rules.append(rule)
updates = []
for line in lines[dividerIndex+1:]:
    page = [int(i) for i in line.split(',')]
    updates.append(page)



#for each update find the applicable rules, check them, if all pass then add to correctUpdates
correctUpdates = []
for update in updates:
    p_f_na = RuleValidator(update, rules)# check all rules and determine pass/fail/na
    # print (p_f_na)
    if all(result in ('P', 'NA') for result in p_f_na):
        print(update)
        correctUpdates.append(update)

# print(correctUpdates)
# find answer
results = [] # will store middle page numbers of correctly ordered updates
for i in correctUpdates:
    # print('len', len(i))
    middleIndex = int((len(i) - 1)/2)
    # print('middle index', middleIndex)
    # print(i[middleIndex])
    results.append(i[middleIndex])

# # report answer
print('answer:', sum(results))
# print(rules)
# print(updates)