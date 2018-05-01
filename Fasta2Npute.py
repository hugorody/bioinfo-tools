#!/usr/bin/python3

import sys
file1 = sys.argv[1] #concater fasta

MD = "-" #missing data

with open(file1,'r') as f:
    seqs={}
    for line in f:
        line = line.rstrip()
        if line[0] == '>':
            words=line.split()
            name=words[0][1:]
            seqs[name]=''
        else:
            seqs[name] = seqs[name] + line

#verify if all sequences have same length
lengths = []
for i in seqs.items():
    if lengths == []:
        lengths.append(len(i[1]))
    else:
        if lengths[-1] != len(i[1]):
            print ("lengths are different",lengths[-1],len(i[1]))
            exit()

outNpute = open(sys.argv[1]+".inNPUTE.csv","w")
for i in range(lengths[0]):
    locus = []
    for j in seqs.items():
        locus.append(j[1][i].replace(MD,"?"))

    MDlocus = locus.count("-") #missing data for the locus
    outNpute.write(",".join(locus) + "\n")
outNpute.close()


headNpute = open(sys.argv[1]+".inNPUTE.header","w")
listkeys = []
for i in seqs.keys():
    listkeys.append(i)

headNpute.write(",".join(listkeys))
headNpute.close()
