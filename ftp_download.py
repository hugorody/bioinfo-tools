#!/usr/bin/python3

import ftplib
import time

myftp = "ftp.pride.ebi.ac.uk"
mydir = "pride/data/archive/2018/01/PXD007893"

# Project PXD007893
# Title: Cell wall proteome of sugarcane young and mature leaves and stems

ftp = ftplib.FTP(myftp)
ftp.login()

ftp.cwd(mydir)

data = []

ftp.dir(data.append)
for line in data:
    myfile = line.split(" ")[-1]
    if "xml" in myfile:
        print ("Downloading: " , myfile)

        with open(myfile,"wb") as f:
            ftp.retrbinary('RETR ' + str(myfile), f.write)
        time.sleep(2)

ftp.quit()
