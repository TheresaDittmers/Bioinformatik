Dna = ['TTACCTTAAC', 'GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG', 'CGTCAGAGGT']
pattern = 'AAA'

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

print('input:', 'DNA:', Dna, ',', 'Pattern:', pattern)
print('output:', 'Distance between pattern and strings:', distancebetweenpatternandstrings(pattern, Dna))
