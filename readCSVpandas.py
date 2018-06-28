#!/usr/bin/python3

import pandas as pd

protclass = {} #final dict with dataframe of pandas

set1 = pd.read_csv("CLASSIFICACAO_PROTEÍNAS_1904.csv") #read the csv file

columnscsv = [] #list of columns keys
for i in set1: #read the keys of columsn
    columnscsv.append(i)

for index, row in set1.iterrows():
    if row["seqname"] in names:
        valuesprotclass = []
        for i in columnscsv[1:]: #for each column starting in 1, append values to list as string
            valuesprotclass.append(str(row[i]))
        protclass[names[row["seqname"]]] = valuesprotclass #create a dict with the values
