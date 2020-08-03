''' transcribing DNA into RNA: given a DNA string t with max length 1000 nt, returns the transcribed RNA string of t
'''

f = open("rosalind_rna.txt", "r") 

t = f.readline().strip()

rna = t.replace("T", "U")

print(rna)
