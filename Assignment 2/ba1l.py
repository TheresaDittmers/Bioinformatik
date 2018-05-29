pattern = 'AGT'
symboltonumber = {'A':0, 'C':1, 'G':2, 'T':3}

def patterntonumber(pattern):
    if pattern == '':
        return 0

    symbol = pattern[-1]
    prefix = pattern[0:-1]

    return 4 * patterntonumber(prefix) + symboltonumber[symbol]

print('input:',     pattern)
print('output:',    patterntonumber(pattern))
