
def IsItSafe(report):
    levels = report
    check_inc = []
    check_dec = []
    
    # check if decreasing
    for index, level in enumerate(levels):
        if index == 0: continue
        elif levels[index-1] - level in range(1,4):
            check_dec.append(True)
        else:
            check_dec.append(False)

    # check if increasing
    for index, level in enumerate(levels):
        if index == 0: continue
        elif levels[index-1] - level in range (-3,0):
            check_inc.append(True)
        else:
            check_inc.append(False)

    if all(check_inc) or all(check_dec): return True
    else: return False

def ProblemDampener(report):
    output = []
    for index, value in enumerate(report):
        reportLess1 = report.copy()
        reportLess1.pop(index)
        output.append(reportLess1)
    return output


# open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

# format input
reports = []
for line in lines:
    report = [int(i) for i in line.split()]
    reports.append(report)

# find answer
results = []
for report in reports:
    print(report)
    result = IsItSafe(report)
    if result:
        results.append(result)
        print('Safe without removing any levels.')
        continue
    dampenedReports = ProblemDampener(report)
    didDampenerWork = None
    for i in dampenedReports:
        dampenedResult = IsItSafe(i)
        if dampenedResult:
            results.append(dampenedResult)
            didDampenerWork = True
            print('Safe with 1 level removed.')
            break
    if didDampenerWork == None:
        print('Unsafe.')
        results.append(result)


# report answer
# print(results)
print(results.count(True), ' safe reports')