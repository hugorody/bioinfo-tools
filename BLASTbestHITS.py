#!/usr/bin/python3

besthits = {}
with open("input.blastn","r") as set1: #input is blast output -outfmt 6 format
    for i in set1:
        i = i.rstrip()
        i = i.split("\t")
        query = i[0]
        subje = i[1]
        ident = float(i[2])

        if query not in besthits:
            besthits[query] = [subje,ident]
        else:
            if ident > besthits[query][1]:
                besthits[query] = [subje,ident]

for i in besthits.items():
    print (i[0] + "\t" + i[1][0] + "\t" + str(i[1][1]))
