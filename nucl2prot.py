#!/usr/bin/python3
#translate nucleotide sequences

import sys
from Bio import SeqIO

fileFAS = sys.argv[1] #fasta file

with open(fileFAS,"r") as set2:
    for i in SeqIO.parse(set2, "fasta"):
        #print (i.format("fasta"))
        print (">" + i.id + "\n" + i.seq.translate())
