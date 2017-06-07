#!/usr/bin/python
#Check integrity of fastq Q33 files
#usage: python script.py file.fastq
 
import sys

filefastq = sys.argv[1]
 
#open file
try:
    fgen = open(filefastq)
except IOError:
    print ("FASTQ file doesn't exist!")

#Create dictionary containing only the fastq sequences which headers are not in the reads list 
seqs={}
parsing = 0
for i in fgen:
    i = i.rstrip()

    if "@" in i[0]:
        scafid = i.split()[0][1:]
     
    if parsing > 0 and "@" not in i[0]:  #Second 2: if parsing is greater than 0, than this is the first line of fastq belonging to a read selected in the first step. When it finds a line with "@", then parsing will be set to 0 and loop starts again
        seqs[scafid] = seqs[scafid] + i
    else:
        parsing = 0

    if "@" in i[0]:  #First 1: if id read are not in my reads list, then parsing will be set 1
        seqs[scafid] = ''  #create a dictionary with the fastq sequence correspondent to the read not in reads list
        parsing += 1

#length seqs
lenseqsdict = {} #dictionary containing read length as keys and the number of reads with that length as values
for i in seqs.items():
    header= i[0]
    info = i[1].split("+")
    lenseq = len(info[0])
    quality = info[1]
    #print "@"+header+"\n"+seq.replace("+", "\n+\n")

    #feed length seqs dictionary
    if lenseq not in lenseqsdict:
        lenseqsdict[lenseq] = 1
    else:
        newlen = int(lenseqsdict[lenseq]) + 1
        lenseqsdict[lenseq] = newlen


#PRINT RESULTS
for i in lenseqsdict.items():
    print filefastq,"has",i[1],"sequences of length",i[0],"bp"