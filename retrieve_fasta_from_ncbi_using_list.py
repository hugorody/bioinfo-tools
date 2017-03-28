#!/usr/bin/python

from Bio import Entrez
from urllib2 import HTTPError
import time
import sys

fileheaders = sys.argv[1]

Entrez.email ="eigtw59tyjrt403@gmail.com"
f = open(fileheaders)

for line in iter(f):
    try:
        handle = Entrez.efetch(db="protein", id=line, retmode="xml")
    except HTTPError:
        time.sleep(20)
        handle = Entrez.efetch(db="protein", id=line, retmode="xml")
    records = Entrez.read(handle)
    print ">"+line.rstrip()+" "+records[0]["GBSeq_primary-accession"]+" "+records[0]["GBSeq_definition"]+"\n"+records[0]["GBSeq_sequence"]
    #time.sleep(1) # to make sure not many requests go per second to ncbi
f.close()
