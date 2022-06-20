# AWK-syntax -filtering and manipulation of sequences
Basic syntax of filtering /manipulating files using awk

function
  - extract/filter, wrangle, compare and transform data
  - work on delimited data
  - reads file line by line
  - splits the file into fields - allows for columns
  - allows one to manipulate features unlike sed it allows to work with columns
 
 ###awk -F "\t" {print $n} inpute_file

e.g. 
### to print out the number of fields/columns in a file anopheles.gff3, this prints the output on screen, should be 9, tab delimited
awk -F "\t" {print $NF} anopheles.gff3

### to direct the the number of fields/columns in a file anopheles.gff3 to another output file
awk -F "\t" {print $NF} anopheles.gff3 > anopheles_columns.txt





 

