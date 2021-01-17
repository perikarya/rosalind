''' inferring mRNA from protein: given a protein string of length at most 1000 aa, returns the total number of different RNA strings from which the protein could have been translated, modulo 1,000,000
'''

codons = {"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V", "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V", "UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V", "UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V", "UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A", "UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A", "UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A", "UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A", "UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D", "UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D", "UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E", "UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E", "UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G", "UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G", "UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G", "UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"}

codons_per_aa = {}

for codon, residue in codons.items():
    if residue in codons_per_aa:
        codons_per_aa[residue] += 1
    else:
        codons_per_aa[residue] = 1

codon_count_list = []

with open("rosalind_mrna.txt") as dataFile:

    aa_seq = dataFile.read().replace("\n", "")

for aa in aa_seq:
    print(aa)
    codon_count_list.append(codons_per_aa[aa])

codon_count_list.append(3) # there are three stop codons signalling the end of translation

from functools import reduce
possibilities = reduce(lambda x, y: x*y, codon_count_list)

result = possibilities % 1000000
print(result)
