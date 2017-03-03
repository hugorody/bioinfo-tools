#!/usr/bin/python
#usage: python script.py file.fasta
#read fasta file with multiple sequences and split, creating one new file for each sequence

import sys

filefasta = sys.argv[1]

try:
    f = open(filefasta)
except IOError:
    print ("File doesn't exist!")


#cria o dicionario para receber as sequencias fasta
seqs={}
for line in f:
    line = line.rstrip()
    if line[0] == '>':
        words=line.split() 
        name=words[0][1:]
        seqs[name]=''
    else:
        seqs[name] = seqs[name] + line


for i in seqs.items():
	header= i[0]
	seq = i[1]
	fo = open(header+".fasta", "w")
	fo.write(">"+header+"\n"+seq);
	print ">"+header+"\n"+seq
	fo.close()
