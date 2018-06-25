Dna = 'CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT', 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA'
k = 8
t = 5

import random

def symboltonumber(symbol):
    if symbol == 'A':
        return 0
    if symbol == 'C':
        return 1
    if symbol == 'G':
        return 2
    if symbol == 'T':
        return 3

def numbertosymbol(index):
    if index == 0:
        return 'A'
    if index == 1:
        return 'C'
    if index == 2:
        return 'G'
    if index == 3:
        return 'T'

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

def profilemostprobable(text, k, profile):
    maxprob = 0
    kmer = text[0:k]
    for i in range(2, len(text)-k+1):
        prob = 1
        pattern = text[i:i+k]
        for j in range(k):
            l = symboltonumber(pattern[j])
            prob *= profile[l][j]
        if prob > maxprob:
            maxprob = prob
            kmer = pattern
    return kmer

def createprofile(motifs):
    k = len(motifs[0])
    profile = [[1 for i in range(k)] for j in range(4)]
    for x in motifs:
        for i in range(len(x)):
            j = symboltonumber(x[i])
            profile[j][i] += 1
        for x in profile:
            for i in range(len(x)):
                x[i] = x[i]/len(motifs)
    return profile

def consensus(profile):
    string = ''
    for i in range(len(profile[0])):
        max = 0
        loc = 0
        for j in range(4):
            if profile[j][i] > max:
                loc = j
                max = profile[j][i]
        string += numbertosymbol(loc)
    return string

def score(motifs):
    profile = createprofile(motifs)
    cons = consensus(profile)
    score = 0
    for x in motifs:
        for i in range(len(x)):
            if cons[i] != x[i]:
                score += 1
    return score

def randomizedmotifsearch(Dna, k, t):
    bestmotifs = []
    motifs = []
    for x in range(t):
        random.seed()
        i = random.randint(0, len(Dna[x])-k)
        motifs.append(Dna[x][i:i+k])
    bestmotifs = motifs.copy()
    count = 0
    while True:
        profile = createprofile(motifs)
        for x in range(t):
            motifs[x] = profilemostprobable(Dna[x], k, profile)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs.copy()
            count += 1
        else:
            print(count)
            return bestmotifs

print('DNA', ':', Dna)
print('k', ':', k)
print('t', ':', t)
print('RandomizedMotifSearch', ':', randomizedmotifsearch(Dna, k, t))















