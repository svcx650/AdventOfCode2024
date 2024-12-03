snafuKey = {'1': 1, '2': 2, '0': 0, '-': -1, '=': -2}
def SNAFUtoDecimal(snafu):
    deciphered = []
    multiplier = 1
    for digit in reversed(snafu):
        deciphered.append(snafuKey[digit] * multiplier)
        multiplier = multiplier * 5
    return sum(deciphered)

def DecimaltoSNAFU(decimal):
    decimalKey = {v: k for k, v in snafuKey.items()}
    deciphered = []
    number = decimal
    i = 1

    while number != 0:
        remainder = number % 5 ** i
        print(remainder)
        if remainder > 2:
            remainder -= 5
        deciphered.append(remainder)
        number -= remainder
        i += 1

    '''for i in range(20, 0, 1):
        remainder = decimal % (2 * 5 ** i)
        if remainder == decimal:
            remainder = decimal % (1 * 5 ** i)
            if remainder == decimal: continue
            deciphered.append(1)# add things to do when a valid 'reducer' is found

        deciphered.append(2) # add things to do when a valid 'reducer' is found
        
        if remainder == 0: break
        # add the clean up before the next loop
        '''
    print('deciphered: ', deciphered)
    # deciphered = deciphered[::-1] # reverse deciphered direction # accomplished with reversed()
    # go from deciphered to encoded via decimalKey
    snafu = ''
    for i in reversed(deciphered):
        snafu = snafu + decimalKey[i]
    return snafu

# open input
with open('testinput.txt', 'r') as file:
    lines = file.read().splitlines()

results = []
for line in lines:
    result = SNAFUtoDecimal(line)
    # print(line, ' to ', result)
    results.append(result)

print('target number: ', sum(results))
translatedResult = DecimaltoSNAFU(sum(results))

# report
# print(sum(results))
print(translatedResult)
