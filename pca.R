#Goal: draw a graph that shows how the samples are related (or not related) to each other
#script prepared from: https://youtu.be/0Jp4gsfOLMs

#Input: samples = columns, variables = rows
fpkm <- read.delim("rnaseq_fpkm.tsv", row.names=1)

filename = "Treatment IAC"

pca <- prcomp(t(fpkm[7:12])) #determine the range of columns 1:6 (SP), 7:12 (IAC), 13:18 (RB05), 19:24 (RB200)
#prcomp expects the samples to be rows and genes to be columns. t() function transposes the input matrix
#prcomp returns: x, sdev, rotation
# x: contains the principal components (PCs). Number of PCs = Number of samples

plot(pca$x[,1], pca$x[,2]) #create the PCA plot with PC1 in X and PC2 in Y axis.

#Determine how much variation each principal component accounts for
#if PC1 and/or PC2 accounts for the largest variation of the data, it means that the plotted graph is meaningful
pca.var <- pca$sdev^2 #calculate how much variation in the original data each PC accounts for
pca.var.per <- round(pca.var/sum(pca.var)*100, 1) #percent of variation of each PC
barplot(pca.var.per, main = "Scree Plot", xlab = "Principal component", ylab = "Percent variation")

#Creating plots with ggplot2
library(ggplot2)

pca.data <- data.frame(Sample=rownames(pca$x), X=pca$x[,1], Y=pca$x[,2])

Experiment <- c("Inoculated","Inoculated","Inoculated","Control","Control","Control")

ggplot(data=pca.data, aes(x=X, y=Y, label=Sample))+
  geom_point(size=7, aes(color=Experiment))+
  geom_text(size=5, color="black", nudge_x = 1500, nudge_y = -200) + #plot the labels
  scale_colour_manual(values=c("#3399FF", "#CC3300"))+
  xlab(paste("PC1 ", pca.var.per[1], "%", sep=""))+ # percentage of the varition in the original data that PC1 accounts for
  ylab(paste("PC2 ", pca.var.per[2], "%", sep=""))+ # percentage of the varition in the original data that PC2 accounts for
  theme_bw()+ #graph background white
  ggtitle(filename)+
  theme(legend.text = element_text(colour="black", size=12))+
  theme(legend.title = element_text(colour="black", size=12, face="bold"))+
  theme(axis.text=element_text(size=12), axis.title=element_text(size=14,face="bold"))+
  theme(plot.title = element_text(size=14,face="bold"))+
  theme(axis.line = element_line(size = 0.5, colour = "black"))

#Examine loading scores to determine what variables have the largest effect on the graph
#find which genes has largest effect in where the samples are plotted

#genes that push samples to the left side of the graph will have negative values
#genes that push samples to the right side of the graph will have positive values
loading_scores <- pca$rotation[,2] #1 for PC1, 2 for PC2, PC3...
gene_scores <- abs(loading_scores) #uses absolute values rather than from high to low
gene_score_ranked <- sort(gene_scores, decreasing = TRUE)
top30_genes <- names(gene_score_ranked[1:30]) #get the top 30 genes with the largest loading score magnitudes

top30scores <- pca$rotation[top30_genes,1] #show the scores (and +/- sign)

write.table(top30scores, file = paste(filename , ".top30.list"), sep = "\t", col.names = TRUE, qmethod = "double")
