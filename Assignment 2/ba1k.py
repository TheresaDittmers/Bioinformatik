text = 'ACGCGGCTCTGAAA'
symboltonumber = {'A':0, 'C':1, 'G':2, 'T':3}
k = 2

def patterntonumber(text):
    if text == '':
        return 0

    symbol = text[-1]
    prefix = text[0:-1]

    return 4 * patterntonumber(prefix) + symboltonumber[symbol]

def frequencyarray(text, k):
    array = [0] * (4**k)
    for i in range(0, (len(text)-k+1)):
        pattern = text[i:i+k]
        j = patterntonumber(pattern)
        array[j] = array[j] + 1
    return array

print('input:',     'text =',text,',',  'k =', k)
print('output:',    frequencyarray(text, k))
