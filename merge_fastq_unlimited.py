#!/usr/bin/python
#usage: python script.py file1.fq file2.fq file3.fq ...fq output.fq
#the last element of sys.argv is the output name

import sys

outputname = sys.argv[len(sys.argv)-1]
output = open(outputname,'w')

for i in sys.argv[1:-1]:
    with open(i) as fastq:
        for j in fastq:
            output.write(j.rstrip()+"\n")
