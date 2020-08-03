''' translating RNA into protein: given an RNA string s corresponding to a strand of mRNA (max length 10 kbp), returns the protein string encoded by s based on the RNA codon table
'''

codons = {"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V", "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V", "UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V", "UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V", "UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A", "UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A", "UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A", "UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A", "UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D", "UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D", "UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E", "UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E", "UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G", "UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G", "UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G", "UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"}

with open("rosalind_prot.txt") as dataFile:

    rna = dataFile.read().replace("\n", "")

    aa = []

    index = 0
    for base in rna:
        codon = rna[index:index+3]
        if len(codon) == 3:
            if codons[codon] == "Stop":
                aa.append("\n")
            else:
                aa.append(codons[codon])
        index += 3
        
    prot = "".join(aa)
    print(prot)
