blastn -query file.fas -db file.db -evalue 10 -word_size 11 -max_target_seqs 50 -gapopen 5 -gapextend 2 -penalty -3 -reward 2 -outfmt 6 -out file.blastn
