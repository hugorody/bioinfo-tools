#!/usr/bin/python3

import sys
from Bio import SeqIO

fileIDS = sys.argv[1] #file with ids separated by breaklines
fileFAS = sys.argv[2] #fasta file

#create a list IDS
listIDS = []
with open(fileIDS) as set1:
    for i in set1:
        i = i.rstrip()
        listIDS.append(i)

#for each ID in list
with open(sys.argv[2],"r") as set2:
    for i in SeqIO.parse(set2, "fasta"):
        if i.id in listIDS:
            print (i.format("fasta"))
