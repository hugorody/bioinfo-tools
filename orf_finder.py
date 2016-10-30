#!/usr/bin/python
#usage: python script.py file.fasta
import sys

filefasta = sys.argv[1]

try:
    f = open(filefasta)
except IOError:
    print ("File doesn't exist!")


#FUNCTION START
def orfFINDER(dna,frame):
    
    stop_codons = ['tga', 'tag', 'taa']
    start_codon = ['atg']
    start_positions = []
    stop_positions = []
    num_starts=0
    num_stops=0
    
    
    for i in range(frame,len(dna),3):
        codon=dna[i:i+3].lower()
        if codon in start_codon:
            start_positions += str(i+1).splitlines()
        if codon in stop_codons:
            stop_positions += str(i+1).splitlines()
    
    for line in stop_positions:
        num_stops += 1
    
    for line in start_positions:
        num_starts += 1
    
    orffound = {}
    
    if num_stops >=1 and num_starts >=1: #first statment: the number of stop codons and start condos are greater than or equal to 1;
        
        orfs = True
        stop_before = 0
        start_before = 0
        
        if num_starts > num_stops:
            num_runs = num_starts
        if num_stops > num_starts:
            num_runs = num_stops
        if num_starts == num_stops:
            num_runs = num_starts
            
        position_stop_previous = 0
        position_start_previous = 0
        counter = 0
        
        for position_stop in stop_positions:
            
            position_stop = int(position_stop.rstrip()) + 2
            
            for position_start in start_positions:
                
                position_start = position_start.rstrip()
                
                if int(position_start) < int(position_stop) and int(position_stop) > int(position_stop_previous) and int(position_start) > int(position_stop_previous):
                    
                    counter += 1
                    nameorf = "orf"+str(counter)
                    position_stop_previous += int(position_stop) - int(position_stop_previous)
                    position_start_previous += int(position_start) - int(position_start_previous)
                    sizeorf = int(position_stop) - int(position_start) + 1
                    
                    orffound[nameorf] = position_start,position_stop,sizeorf,frame
                        
                else:
                    
                    pass
    
    else:
        
        orfs = False

    return orffound
#FUNCTION END


#READ FASTA FILE AND SAVE HEADERS AND SEQUENCES IN A DICTIONARY
seqs={}

for line in f:
    line = line.rstrip()
    if line[0] == '>':
        words=line.split() 
        name=words[0][1:]
        seqs[name]=''
    else:
        seqs[name] = seqs[name] + line
        
#DEFINE FRAME TO FIND ORF
#if frame = 0, start from the first position in the sequence
frame=0

#EXECUTE THE ORFFINDER FUNCTION
for i in seqs.items():
    header= i[0]
    seq = i[1]
    orf = orfFINDER(seq,frame)
    
    for i in orf.items():
        numorf=i[0]
        startorf=orf[numorf][0]
        stoporf=orf[numorf][1]
        lengthorf=orf[numorf][2]
        frameorf=orf[numorf][3]
        print header,numorf,"start",startorf,"stop",stoporf,"length",lengthorf,"frame",frameorf

f.close()
