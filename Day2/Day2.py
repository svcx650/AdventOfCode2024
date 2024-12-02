
def IsItSafe(report):
    levels = [int(i) for i in report.split()]
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


# open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

# format input


# find answer
count = 0
results = []
for line in lines:
    result = IsItSafe(line)
    results.append(result)
    if result: count += 1

# report answer
print(results)
print(count, ' safe reports')