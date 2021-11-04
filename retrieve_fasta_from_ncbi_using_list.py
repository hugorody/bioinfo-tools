#!/usr/bin/python3

from Bio import Entrez
#from urllib2 import HTTPError
import time
import sys

fileheaders = sys.argv[1]

Entrez.email ="eigtw59tyjrt403@gmail.com"
f = open(fileheaders)

headers = {}
with f as set1:
    for i in set1:
        i = i.rstrip().split("\t")
        headers[i[0]] = ''


for line in headers.keys():
    try:
        handle = Entrez.efetch(db="protein", id=line, retmode="xml")
    except HTTPError:
        time.sleep(20)
        handle = Entrez.efetch(db="protein", id=line, retmode="xml")
    records = Entrez.read(handle)
    print (">"+line+" "+records[0]["GBSeq_primary-accession"]+" "+records[0]["GBSeq_definition"]+"\n"+records[0]["GBSeq_sequence"].upper())
    time.sleep(1) # to make sure not many requests go per second to ncbi
f.close()
