''' counting DNA nucleotides: given a DNA string of max length 1000 nt, returns four integers (separated by spaces) counting the respective number of times that the nucleotides 'A', 'C', 'G', and 'T' occur in the sequence
'''

f = open("rosalind_dna.txt", "r") 

s = f.readline().strip()

nucleotides = {"A":0, "C":0, "G":0, "T":0}

for i in s:
    if i == "A":
        nucleotides["A"] +=1
    elif i == "C":
        nucleotides["C"] +=1
    elif i == "G":
        nucleotides["G"] +=1
    elif i == "T":
        nucleotides["T"] +=1

print(nucleotides["A"], end=" ")
print(nucleotides["C"], end=" ")
print(nucleotides["G"], end=" ")
print(nucleotides["T"])
