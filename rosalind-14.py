''' given two DNA strings s and t (each of length at most 1 kbp), returns all locations of t as a substring of s
'''

with open("rosalind_subs.txt") as dataFile:

    s, t = dataFile.read().strip().split()

    positions = []

    for n in range(len(s)):
        if s[n:n+len(t)] == t:
            positions.append(n+1) # addition of 1 adjusts for python's 0-indexing

    print(positions)
