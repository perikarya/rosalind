''' given two DNA strings, s and t, of equal length, returns the Hamming distance dH(s,t) defined the by number of corresponding bases that differ between s and t
'''

with open("rosalind_hamm.txt") as dataFile:

    strings = dataFile.read()
    s, t = strings.split()
    
    dist = 0

    for i, base in enumerate(s):
        if s[i] != t[i]:
            dist += 1

    print(dist)
