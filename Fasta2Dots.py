#!/usr/bin/python
#usage: python script.py file.fasta
import sys
 
filefasta = sys.argv[1]
 
try:
    f = open(filefasta)
except IOError:
    print ("File doesn't exist!")
 
seqs={}
 
for line in f:
    line = line.rstrip()
    if line[0] == '>':
        words=line.split()
        name=words[0][1:]
        seqs[name]=''
    else:
        seqs[name] = seqs[name] + line



keylist = seqs.keys()
keylist.sort()

first_header = keylist[0]
first_sequence = seqs[first_header]
 
print first_header,''.join(first_sequence)
 
comparison = {}
 
for i in seqs.items():
    header= i[0]
    seq = i[1]
    if header != first_header:
        comparison[header] = ''
        for i in range(0,len(seq)):
            letter=seq[i]
            base=first_sequence[i]
            if letter == base:
                comparison[header] = comparison[header] + '.'
            else:
                comparison[header] = comparison[header] + letter
 
for i in comparison.items():
    header=i[0]
    seq=i[1]
    print header,seq
