Dna = ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTACGGGACAG']
k = 3

def HammingDistance(string1, string2):
    mismatches = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            mismatches += 1
    return mismatches

def distancebetweenpatternandstrings(pattern, Dna):
    k = len(pattern)
    distance = 0
    for subpattern in Dna:
        Hamming = k+1
        for i in range(len(subpattern)-k+1):
            if Hamming > HammingDistance(pattern, subpattern[i:i+k]):
                Hamming = HammingDistance(pattern, subpattern[i:i+k])
        distance = distance + Hamming
    return distance

def numbertopattern(index, k):
    if k == 1:
        return numbertosymbol(index)
    return numbertopattern(index // 4, k-1) + numbertosymbol(index % 4)

def numbertosymbol(index):
    if index == 0:
        return 'A'
    if index == 1:
        return 'C'
    if index == 2:
        return 'G'
    if index == 3:
        return 'T'

def medianstring(Dna, k):
    distance = (k+1) * len(Dna)
    median = ''
    for i in range(4**k):
        pattern = numbertopattern(i,k)
        if distance > distancebetweenpatternandstrings(pattern, Dna):
            distance = distancebetweenpatternandstrings(pattern, Dna)
            median = pattern
    return median

print('input:', 'DNA:', Dna, ',', 'k:', k)
print('output:', 'Median String:', medianstring(Dna, k))

