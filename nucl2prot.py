#!/usr/bin/python3
#translate nucleotide sequences

import sys
from Bio import SeqIO

fileFAS = sys.argv[1] #fasta file

output = open(fileFAS+".nucl2prot.fas","w")

with open(fileFAS,"r") as set2:
    for i in SeqIO.parse(set2, "fasta"):
        #print (i.format("fasta"))
        output.write (">" + str(i.id) + "\n" + str(i.seq.translate()).replace("\*",""))
