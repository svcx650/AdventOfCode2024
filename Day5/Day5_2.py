def RuleValidator(update, rules):
    ####### checks an update for pass/fail/NA to all rules
    passed = []
    failed = []
    for rule in rules:
        # check that update contains both pages otherwise NA
        try:
            a = update.index(rule[0])
            b = update.index(rule[1])
            if a < b:
                passed.append(rule)
            else: failed.append(rule)
        except ValueError:
            continue
    return passed, failed



def Reorder(update, passes, fails):
    ####### corrects the pages in an update to comply with all applicable rules
    applicableRules = passes + fails
    passHistory = [passes]
    orderedUpdate = update
    attempt = 0
    moveY = True
    while len(fails) > 0:
        # make changes to update to be more correctly ordered
        for rule in applicableRules:

            a = orderedUpdate.index(rule[0]) # X and Y are the numbers, a is the index of X and b is index of Y
            b = orderedUpdate.index(rule[1])
            if a < b:
                continue
            else:
                if moveY:
                    # move Y to be true
                    orderedUpdate.insert(a + 1, rule[1]) # inserts what is now a second instance of Y
                    orderedUpdate.remove(rule[1]) # removes first instance of Y
                else: 
                    # move x to be true
                    orderedUpdate.insert(b - 1, rule[0]) # inserts what is now a second instance of Y
                    orderedUpdate.remove(rule[0]) # removes first instance of Y


        # check changes and repeat if necessary
        passes, fails = RuleValidator(update, applicableRules)
        passHistory.append(passes)
        attempt += 1
        ## the below if statements didn't end up being necessary, after thinking about it more I think with enough iterations (assuming solvable rules) the above will always work.
        if attempt > 1000:
            print('switching to moveX, update',update, 'is currently', orderedUpdate)
            moveY = False
        if attempt > 2000:
            print('max attempts reached, update',update, 'is currently', orderedUpdate)
            print(passHistory)
            return None
    # print(attempt, 'attempts needed to solve update', update)
    return orderedUpdate



# open and format input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

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

allUpdates = [] # each element will have 3 lists, update, passed rules, failed rules
for update in updates:
    passes, fails = RuleValidator(update, rules)
    updateInfo = [update, passes, fails]
    allUpdates.append(updateInfo)
        
incorrectUpdates = []
for info in allUpdates:
    if len(info[2]) != 0:
        incorrectUpdates.append(info)

# find answer
results = [] # will store middle page numbers of correctly ordered updates
for i in incorrectUpdates:
    reorderdUpdate = Reorder(i[0],i[1],i[2])
    middleIndex = int((len(reorderdUpdate) - 1)/2)
    results.append(reorderdUpdate[middleIndex])

# # report answer
print('answer:', sum(results))