






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

update = []
for line in lines[dividerIndex+1:]:
    page = [int(i) for i in line.split(',')]
    update.append(page)

#for each 


# # find answer
# countxmases = 0
# for matrix in rotatedinput:
#     increment = 0
#     for line in matrix:
#         increment = 0
#         increment = FindXMAS(line)
#         countxmases += increment
#         print(increment)


# # report answer
# print('Total Count:', countxmases)