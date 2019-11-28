#!/usr/bin/sh
#usage: sh sam_to_graphic_viewer_input.sh reference.fasta file.sam
#Generate required inputs for the visualization of NGS assambly in Tablet software https://ics.hutton.ac.uk/tablet/download-tablet/

######### SAMTOOLS dependencies
#sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe" 
#sudo apt-get update
#sudo apt-get install libncurses5-dev
#sudo apt-get install libbz2-dev
######### SAMTOOLS installation
#Download at https://sourceforge.net/projects/samtools/files/samtools/1.4.1/
#./configure
#make
#sudo make install

reference=`echo "$1"`
samfile=`echo "$2"`
name=`echo "$samfile" | sed "s/.sam//g"`

samtools faidx "$reference"  #creates index *.fai
samtools view -bt "$reference".fai "$samfile" > "$name".bam
samtools sort "$name".bam > "$name"_sorted.bam
samtools index "$name"_sorted.bam  #creates index *.bai
