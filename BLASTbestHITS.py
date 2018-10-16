#!/usr/bin/python3

import numpy as np

blastinput = "input.blastn"

besthit = {}
with open(blastinput,"r") as set1:
    for i in set1:
        i = i.rstrip()
        i = i.split("\t")
        query = i[0]
        subje = i[1]
        ident = float(i[2])
        align = float(i[3])
        evalu = float(i[10])

        if query != subje:

            if query not in besthit:
                besthit[query] = [subje,ident,align,evalu]
            else:
                if ident > besthit[query][1]:
                    if align > besthit[query][2]:
                        besthit[query] = [subje,ident,align,evalu]
                else:
                    if align > besthit[query][2] and evalu < besthit[query][3]:
                        besthit[query] = [subje,ident,align,evalu]

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
