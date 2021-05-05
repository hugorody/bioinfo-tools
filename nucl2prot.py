#!/usr/bin/python3
#translate nucleotide sequences

import sys
from Bio import SeqIO

fileFAS = sys.argv[1] #fasta file

output = open(fileFAS+".prot.fas","w")

with open(fileFAS,"r") as set2:
    for i in SeqIO.parse(set2, "fasta"):
        id = str(i.id)
        seq = str(i.seq.translate())
        output.write(">"+id+"\n"+seq+"\n")
