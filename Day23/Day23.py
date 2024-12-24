def AddIfUnique(newSublist, lists):
    newSet = set(newSublist)
    if not any(newSet == set(sublist) for sublist in lists):
        lists.append(newSublist)
    return lists

### open input
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

### format input

### find answer
parties = []
for line in lines:
    a, b = line.split('-')

    # check all lines for connections to each computer
    a_connections = []
    b_connections = []
    for nextline in lines:
        if nextline == line: continue
        if a in nextline.split('-'):
                a_connections.append(nextline)
        if b in nextline.split('-'):
                b_connections.append(nextline)
    # print('a_connections', a_connections)
    # print('b_connections', b_connections)
    for computer in a_connections:
        try:
            c = next(value for value in computer.split('-') if value != a)
        except StopIteration:
            print('no c found')
            continue 
        # find c in b_connections
        for comp in b_connections:
            if c in comp.split('-'):
                # check if combination has already been added to parties, if not then append
                parties = AddIfUnique([a, b, c], parties)
                # print('parties', parties)
        

# 1st comp - 2nd comp
# For I in remaining items
#     If either matches 1st comp add to list
# Check list for 2nd comp

# Filter for comps that start with t
# Count and return answer


### report answer
t_parties = [ party for party in parties if any(computer[0] == 't' for computer in party) ]
print('Answer:', len(t_parties))