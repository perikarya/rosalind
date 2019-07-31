f = open("rosalind_revc.txt", "r") 

s = f.readline().strip()

r = s[::-1]

rc = ""

for i in r:
    if i == "A":
        rc += "T"
    elif i == "T":
        rc += "A"
    elif i == "G":
        rc += "C"
    elif i == "C":
        rc += "G"
        
print(rc)
