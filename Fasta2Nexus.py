#!/usr/bin/python
#usage: python script.py input.fasta output.nexus

import sys

filefasta = sys.argv[1]
outputname = sys.argv[2]

try:
    f = open(filefasta)
except IOError:
    print ("File doesn't exist!")

#create dictionary with all fasta sequences
seqs={}
for line in f:
    line = line.rstrip()
    if line[0] == '>':
        words=line.split() 
        name=words[0][1:]
        seqs[name]=''
    else:
        seqs[name] = seqs[name] + line


nchar = len(seqs.values()[0])
ntax = len(seqs)

output1 = open(outputname, "w")

output1.write("#NEXUS\nbegin data;\n\tdimensions ntax="+str(ntax)+" nchar="+str(nchar)+";\n\tformat datatype=dna missing=? gap=- interleave;\nmatrix\n");   #write header in output1

for i in sorted(seqs.items()):
	head = i[0]
	seq = i[1]
	
	output1.write(head+"\t\t"+seq+"\n");
	

output1.write("\n\n;\nend;");
