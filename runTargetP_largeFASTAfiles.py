#!/usr/bin/python3
#Parse FASTA files containing large number of sequences (>100 seqs),
#split the file into multiple files, run TargetP for each file generated
#and create a unique final TargetP output.

import sys
import subprocess
from Bio import SeqIO

outputname = "file.targetP"
filefasta = "file.fasta"

targetPdic = {}
seqs = []
with open(filefasta,"r") as set1:
    for j in SeqIO.parse(set1,"fasta"):
        seqID = str(j.id)
        seq = str(j.seq)
        seqs.append(">"+seqID+"\n"+seq+"\n")

x = 1
iteration = 100
count = 0
for i in range(0, len(seqs), iteration):
    outfasta = open("target_sequence.fas","w")
    print ("Writing fasta")
    if iteration*x < len(seqs):
        maxval = iteration*x
    else:
        maxval = len(seqs)
    for j in range(i, maxval):
        outfasta.write(seqs[j])
    x += 1
    outfasta.close()
    #run targetP
    targetP = subprocess.Popen('./targetp -P target_sequence.fas > targetp_seq_result.tmp',shell = True)
    targetP.wait()

    #with result of targetP
    with open("targetp_seq_result.tmp","r") as set_inside:
        for i in set_inside:
            i = i.rstrip().split()
            if len(i) == 8 and i[0] != "Name":
                targetPdic[count] = i
                count += 1
                print (" ".join(i))

    #delete temporary targetp for sequence
    targetP_tmp_del = subprocess.call('rm targetp_seq_result.tmp',shell = True)

print ("Writing file targetP.result.txt")
outtargetP = open(outputname,"w")
outtargetP.write("Name                  Len     cTP    mTP     SP  other  Loc  RC\n"+
                "----------------------------------------------------------------------\n")
for i in targetPdic.items():
    outtargetP.write("\t".join(i[1])+"\n")
print ("Done!")
