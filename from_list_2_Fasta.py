#!/usr/bin/python
#usage: python script.py file.fasta filelist.txt
#read a file with list of headers and captures the correspondent fasta sequences in the file fasta multi-lines

import sys

filefasta = sys.argv[1]
filelist = sys.argv[2]

try:
    f = open(filefasta)
except IOError:
    print ("File doesn't exist!")

set_list = set(line.strip() for line in open (filelist, 'r'))

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

#read list of headers to get correspondent fasta sequences
for line1 in set_list:
	for i in seqs.items():
		header= i[0]
		seq = i[1]
		
		if line1 in header:

			print ">"+line1+"\n"+seq+"\n"
