text = 'ACGCGGCTCTGAAA'
symboltonumber = {'A':0, 'C':1, 'G':2, 'T':3}
k = 2

def patterntonumber(text):
    if text == '':
        return 0

    symbol = text[-1]
    prefix = text[0:-1]

    return 4 * patterntonumber(prefix) + symboltonumber[symbol]

def numbertopattern(index, k):
    if k == 1:
        return numbertosymbol(index)

    prefixindex = index // 4
    r = index % 4
    symbol = numbertosymbol(r)
    prefixpattern = numbertopattern(prefixindex, k-1)

    return prefixpattern + symbol

def numbertosymbol(index):
    if index == 0:
        return 'A'
    if index == 1:
        return 'C'
    if index == 2:
        return 'G'
    if index == 3:
        return 'T'

def computingfrequencies(text, k):
    frequencyarray = [0] * (4**k)
    for i in range(0, (len(text)-k+1)):
        pattern = text[i:i+k]
        j = patterntonumber(pattern)
        frequencyarray[j] = frequencyarray[j] + 1
    return frequencyarray

def fasterfrequentwords(text, k):
    frequentpatterns = []
    frequencyarray = computingfrequencies(text, k)
    maxcount = max(frequencyarray)
    for i in range(0, (4**k)-1):
        if frequencyarray(i) == maxcount:
            pattern = numbertopattern[i:k]
            frequentpatterns.append(pattern)
    return frequentpatterns

def frequentwords(text, k):
    frequentpatterns = []
    count = [0] * len(text)
    for i in range(0, (len(text) - k + 1)):
        pattern = text[i:i+k]
        count[i] = patterncount(text, pattern)
    m = max(count)
    for i in range(0, (len(text) - k +1)):
        if count[i] == m:
            if text[i:i+k] not in frequentpatterns:
                frequentpatterns.append(text[i:i+k])
    return frequentpatterns

def patterncount(text, pattern):
    count = 0
    for i in range(0, (len(text) - len(pattern)) + 1):
        if text[i:i+len(pattern)] == pattern:
            count = count + 1
    return count

print('input:',     'text =',text,',',  'k =', k)
print('output:',    frequentwords(text, k))
