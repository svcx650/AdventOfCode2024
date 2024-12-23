def FindXMAS(line):  # accepts a string and finds matches of searchCriteria
    countxmases = 0
    countsamxes = 0
    searchIndex = 0
    Criteria = 'XMAS'
    minSearchLength = len(Criteria)
    while searchIndex < len(line): # exits if remaining string cannot contain the criteria
        xmas = line.find(Criteria, searchIndex)
        if xmas != -1:
            countxmases += 1
            # print('found', Criteria,'count is now',countxmases)
            searchIndex = xmas + 1
        else:
            searchIndex = len(line)
            # print(Criteria, 'not found.')
            continue

    Criteria = 'SAMX'
    minSearchLength = len(Criteria)
    searchIndex = 0
    while searchIndex < len(line): # exits if remaining string cannot contain the criteria
        xmas = line.find(Criteria, searchIndex)
        if xmas != -1:
            countsamxes += 1
            # print('found', Criteria,'count is now',countxmases)
            searchIndex = xmas + 1
        else:
            searchIndex = len(line)
            # print(Criteria, 'not found.')
            continue

    return countxmases, countsamxes



### open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
mappedArea = [list(line) for line in lines]


### find answer
field = {} # holds crop type then list with perimeter and area, need to make it so I can have multiple of the same crop type


### report answer
print('Answer:', )