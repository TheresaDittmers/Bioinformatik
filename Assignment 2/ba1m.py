index = 45
k = 4

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

print('input:',     'index =',index,',', 'k =', k)
print('output:',    numbertopattern(index, k))
