f = open("rosalind_rna.txt", "r") 

t = f.readline().strip()

rna = t.replace("T", "U")

print(rna)
