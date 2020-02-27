#This script intends to iterate with multiple-sequence alignment (MSA) FASTA files in a 
#directory and create Neighbor-Joining (NJ) trees for each of those files.

library(ape)
library(phangorn)
 
  
myfiles <- list.files(path = "/path/to/msa/fasta/files/", pattern = NULL, all.files = FALSE,
           full.names = FALSE, recursive = FALSE,
           ignore.case = FALSE, include.dirs = FALSE, no.. = FALSE)
  
for (fastafile in myfiles) {
  
infile <- paste(c("/path/to/msa/fasta/files/",fastafile),collapse="")
outfile <- paste(c(fastafile,".nwk"),collapse="")
  
print (paste(infile))
  
#phangorn
mytree <- read.phyDat(infile,format="fasta", type = "AA")
dm <- dist.ml(mytree)
treeNJ <- NJ(dm)
 
  
#write tree
write.tree(treeNJ, file=outfile) #fastafile.nwk
