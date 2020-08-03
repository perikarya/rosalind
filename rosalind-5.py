''' computing gc content: given a series of DNA strings in FASTA format (in rosalind's implementation, labelled by the ID "Rosalind_xxxx" where "xxxx" denotes a four-digit code), returns the ID of the sequence with the highest GC-content, followed by the GC-content of that string
'''

with open("rosalind_gc.txt") as dataFile:

    data = dataFile.read().split(">")

    dataset = []

    for line in data[1:]:
        line = line.replace("\n", "")
        dataset.append(line)

    dict = {}

    for line in dataset:
        new_key = line[0:13]
        key_val = line[13:]
        dict[new_key] = key_val

    gc_content = {}

    for label, sequence in dict.items():
        total_bases = len(sequence)
        gc_bases = 0
        for char in sequence:
            if char == "G" or char == "C":
                gc_bases += 1
        print("here", gc_bases)
        gc_proportion = gc_bases / total_bases * 100
        gc_content[label] = gc_proportion

    print(max(gc_content, key=gc_content.get), "\n", max(gc_content.values()))
