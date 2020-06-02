#!/usr/bin/python3

from Bio import SeqIO
import networkx as nx
import re

################################################################################
# INPUT
blastinput = "result.blastp" #file.fasta vs file.fasta BLAST result
fastainput = "file.fasta"

################################################################################
# FILTER BLASTn RESULTS

print ("Parsing FASTA")
seqsize = {} #dictionary with sequence IDs as keys, and sequence len as values
with open(fastainput,"r") as set2:
    for i in SeqIO.parse(set2, "fasta"):
        seq = re.sub(".[0-9]$","",(i.id)).replace(".","") #used to avoid alternatives from A. thaliana
        seqsize[seq] = len(str(i.seq))

output = open(blastinput + ".filtered","w")
print ("Filtering BLAST results")
with open(blastinput,"r") as set1:
    for i in set1:
        i = i.rstrip()
        i = i.split("\t")
        query = re.sub(".[0-9]$","",i[0]).replace(".","")
        subje = re.sub(".[0-9]$","",i[1]).replace(".","")
        ident = float(i[2])
        length = float(i[3])
        mismatch = int(i[4])
        gapopen = int(i[5])
        startquery = int(i[6])
        endquery = int(i[7])
        evalu = float(i[10])
        cov = int(length * 100) / seqsize[query] #parameter given in % of query length

        if query != subje and ident >= 50.0 and cov >= 85: #BLAST Filter
            output.write(query+"\t"+subje+"\t"+"\t".join(i[2:])+"\n")

################################################################################
# MODEL GRAPH
print ("Modeling graph")
G = nx.Graph() # Define the graph and type directed

g = {}
with open(blastinput+".filtered","r") as set1:
    for i in set1:
        i = i.rstrip().split("\t")
        query = i[0]
        subje = i[1]

        if query not in G:
            g[query] = [subje]
        else:
            g[query] = g[query] + [subje]

totalgenes = 0 #count total of genes having paralogs
for i in g.items():
    addnode = G.add_node(i[0])
    totalgenes += len(i[1]) + 1

#add edges
for i in g.items():
    source  = i[0]
    for t in i[1]:
        target = t
        if not G.has_edge(source,target): #verify if edge has not been added
            if not G.has_edge(target,source): #verify if edge has not been added
                addedge = G.add_edge(source,target)

#Export graph
#export_graphml = nx.write_graphml(G, blastinput + ".xml")

#Export subgraphs (groups of paralogs)
#Returns the set of nodes in the component of graph containing node n.
output = open(blastinput+".paralogs.tsv","w")
paralogs_in_networks = {}
for i in G:
    paralogs = [p for p in nx.node_connected_component(G, i) if p != i]
    for p in paralogs:
        if p not in paralogs_in_networks:
            paralogs_in_networks[p] = ''
    output.write (i+"\t"+",".join(paralogs)+"\n")

print ("Paralogs in networks:",len(paralogs_in_networks))
