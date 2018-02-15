#!/usr/bin/python3
#read fasta multiple sequence alignment file and changes stop codons to "---"
#usage: python verifyStopCodon.py file.fasta

import sys

with open(sys.argv[1],"r") as f:

    seqs={}

    for line in f:
        line = line.rstrip()
        if line[0] == '>':
            words=line.split()
            name=words[0][1:]
            seqs[name]=''
        else:
            seqs[name] = seqs[name] + line

seqs_nostopcodon = {}

for j in seqs.items():
    count = 0
    seqs_nostopcodon[j[0]] = ''

    for i in range(0,len(j[1]),3):
        count += 1
        codon = j[1][i:i+3]

        if codon == "TAA" or codon == "TGA" or codon == "TAG":
            codon = "---"
            seqs_nostopcodon[j[0]] = seqs_nostopcodon[j[0]] + codon

        else:
            seqs_nostopcodon[j[0]] = seqs_nostopcodon[j[0]] + codon


for i in seqs_nostopcodon.items():
    print (">"+i[0]+"\n"+i[1]+"\n")
