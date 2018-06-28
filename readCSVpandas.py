#!/usr/bin/python3

import pandas as pd

protclass = {} #final dict with dataframe of pandas

set1 = pd.read_csv("CLASSIFICACAO_PROTEÍNAS_1904.csv") #read the csv file

columnscsv = [] #list of columns keys
for i in set1: #read the keys of each columns in dataframe
    columnscsv.append(i) #append to a list

for index, row in set1.iterrows(): #iterate over rows of pandas dataframe
    valuesprotclass = []
    for i in columnscsv[1:]: #for each column starting in 1, 
        valuesprotclass.append(str(row[i])) #append values in dataframe columns to a list as string
    protclass[row[columnscsv[0]]] = valuesprotclass #create a dict where the keys are the first column, and the values are list with remaining columns of pandas dataframe
