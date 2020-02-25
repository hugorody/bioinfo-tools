#!/usr/bin/python3

from Bio import SeqIO

inputfasta = "file.fasta"
acronym_pre = "Frag_" #prefix acronym for the outputs
sizefile = 50000 #number of sequences per file
countseq = 0
output = 1

outfasta = open(acronym_pre+str(output)+".fa","w")

with open(inputfasta,"r") as set1:
    for i in SeqIO.parse(set1,"fasta"):
        countseq += 1
        if countseq <= sizefile:
            output = output
        else:
            output += 1
            countseq = 0
            outfasta = open(acronym_pre+str(output)+".fa","w")
        
        outfasta.write(">"+str(i.id)+"\n"+str(i.seq)+"\n")
