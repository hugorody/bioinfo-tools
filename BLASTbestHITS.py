#!/usr/bin/python3

import numpy as np
from Bio import SeqIO

fastainput = "file.fas"
blastinput = "blast_output.txt"

seqsize = {}
with open(fastainput,"r") as set2:
    for i in SeqIO.parse(set2, "fasta"):
        seqsize[i.id] = len(str(i.seq))

besthit = {}
with open(blastinput,"r") as set1:
    for i in set1:
        i = i.rstrip()
        i = i.split("\t")
        query = i[0]
        subje = i[1]
        ident = float(i[2])
        align = float(i[3])
        startquery = int(i[6])
        endquery = int(i[7])
        cov = int(align * 100) / seqsize[query] #parameter given in % of query length
        evalu = float(i[10])

        if query != subje:

            if query not in besthit:
                besthit[query] = [subje,ident,align,cov,evalu]
            else:
                if ident >= besthit[query][1] and align > besthit[query][2] and cov > besthit[query][3]:
                        besthit[query] = [subje,ident,align,cov,evalu]

meanidentity = []
meanalignmen = []
for i in besthit.items():
    meanidentity.append(i[1][1])
    meanalignmen.append(i[1][2])

print ("Mean  identity:",np.mean(meanidentity))
print ("Mean align len:",np.mean(meanalignmen))

output = open(blastinput + ".besthit","w")
for i in besthit.items():
    output.write(i[0] + "\t" + "\t".join(map(str,i[1])) + "\n")
