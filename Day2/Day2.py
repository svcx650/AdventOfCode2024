
def IsItSafe(report):
    levels = [int(i) for i in report.split()]
    checks = []
    for level in levels:
        # check:
        # The levels are either all increasing or all decreasing.
        # Any two adjacent levels differ by at least one and at most three.
        # return true if both conditions are met (or store it in checks and return that, but the former is cleaner)

    if True in checks: return True
    else return False


# open input
with open('testinput.txt', 'r') as file:
    reports = file.read().splitlines()



# format input
for report in reports:
    IsItSafe(report)

# report answer
print('result: ',sum(simScores))