#!/usr/bin/perl -w

use strict;
use warnings;

use LWP::Simple;

my $fasta = "";
my $query = "";

my $utils = 'http://www.ncbi.nlm.nih.gov/entrez/eutils/';
my $dbase = 'nucleotide';      #or 'protein'
my $reply = 'fasta';

system ( "clear" );

scalar ( @ARGV ) == 2 or die "\nNumber of parameters must be 2.\n\n\$ perl program_name input_file_name output_file_name\n\n";

open F_INP, "<", $ARGV[0] or die "Can't open file '$ARGV[0]': $!";
open F_OUT, ">", $ARGV[1] or die "Can't open file '$ARGV[1]': $!"; 

while ( <F_INP> ) {
        next if /^$/;    # Blank lines
        next if /^\s+$/; # Lines with only space chars
        next if /^\s*#/; # Just comments
    
        s/(.*)#.*/$1/;
    
        chomp; #exclui o controle de fim de linha
        
        $query = $utils . "efetch.fcgi?db=" . $dbase . "&id=" . $_ . "&rettype=" . $reply;
        
        $fasta = get ( $query );
        
        chomp ( $fasta );
        
        print F_OUT "$fasta\n";
        
        print "\n$query... done!\n";
}

close F_INP;
close F_OUT;

exit;
