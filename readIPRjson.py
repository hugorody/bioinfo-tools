#!/usr/bin/python3

import sys
import json

jsonfile = sys.argv[1]

with open(jsonfile,"r") as set1:
    for i in set1:
        i = i.rstrip()
        myjson = json.loads(i)

for i in myjson["entries"]:
    if "IPR" in i["id"]:
        accession = i["id"]
        name = "".join(i["fields"]["name"])
        description = i["fields"]["description"]
        print (accession,name)
