#!/usr/bin/python3
# Uses tabular output format 6 of BLAST from all vs all searches to find
# groups of orthologs

import networkx as nx

#blastinput is the BLAST(p) output tabular format: -outfmt "6 std qcovs"
blastinput = "file.blastp"
identity_cutoff = 30.0
querycoverage_cutoff = 60.0

# MODEL Directed GRAPH
G = nx.DiGraph() # Define the graph and type directed
with open(blastinput,"r") as set1:
    for i in set1:
        i = i.rstrip().split("\t")
        query = i[0]
        subje = i[1]
        ident = float(i[2])
        length = float(i[3])
        mismatch = int(i[4])
        gapopen = int(i[5])
        startquery = int(i[6])
        endquery = int(i[7])
        startsubje = int(i[8])
        stopsubje = int(i[9])
        evalu = float(i[10])
        bitscore = float(i[11])
        qcov = float(i[12])

        if ident >= identity_cutoff and qcov >= querycoverage_cutoff:
            G.add_node(query)
            G.add_node(subje)
            edge = G.add_edge(query,subje,
                            identity = ident,
                            coverage = qcov)


# REMOVE ALL NON-RECIPROCAL EDGES
edges_to_remove = {}
for u,v in G.edges: #iterate all edges
    if not G.has_edge(v,u): #verify if edge has not its reciprocal
        edges_to_remove[u] = v

for i in edges_to_remove.items():
    G.remove_edge(i[0],i[1]) #if not then remove edge
    print ("Removing edge",i[0],i[1])

# EXPORT GRAPH
#export_graphml = nx.write_graphml(G, "orthogroups.xml")

# EXPORT ORTHOGROUPS AS THE CONNECTED COMPONENTS
G = G.to_undirected()
out = open("orthogroups.txt","w")
count = 0
for i in nx.connected_components(G):
    count += 1
    out.write("GRU"+str(count)+":"+" "+",".join(i)+"\n")
